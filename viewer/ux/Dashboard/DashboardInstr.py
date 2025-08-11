import random
import globals
import numpy as np
from despyner.MessageBox import MessageBox
from ux.MplSpecCanvas import MplSpecCanvas
from despyner.QtMger import set_icon, i_name
from despyner.popupDialog.UXPopupDialog import UXPopupDialog
from single_include import (
    RsInstrument,
    traceback,
    datetime,
    timezone,
    Signal,
    QObject,
    QThread,
    QMessageBox,
    time,
    Slot,
)
from despyner.comboBoxDialog.UXComboBoxDialog import UXComboBoxDialog
from despyner.popupDialog.PopupDialog import Ui_Dialog as UIPopupDialog
from despyner.QtMger import set_icon, i_name, WindowManager, get_icon_path
from despyner.comboBoxDialog.ComboBoxDialog import Ui_Dialog as UIComboBoxDialog


class Worker(QObject):
    progress = Signal(tuple)

    def set_parent(self, par):
        self.__par = par

    def run(self):
        def is_float(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        while True:
            time.sleep(5)
            while self.__par.instr:
                is_instr = isinstance(self.__par.instr, RsInstrument)
                if is_instr and self.__par.instr and self.__par.thread_safe:
                    self.__par.thread_safe = False
                    self.__par.instr.write_str("INIT:IMM")
                    self.__par.thread_safe = True

                time.sleep(self.__par.sweep + 1)

                data = []
                if is_instr:
                    if self.__par.instr and self.__par.thread_safe:
                        self.__par.thread_safe = False
                        data = self.__par.instr.query_str_list("TRACE:DATA?")
                        self.__par.thread_safe = True
                    else:
                        continue
                else:
                    data = [random.random() for _ in range(1000)]

                if data and all(is_float(s) for s in data):
                    start = self.__par.center - self.__par.span
                    stop = self.__par.center + self.__par.span
                    freqs = list(map(lambda x: x, np.linspace(start, stop, len(data))))
                    self.__par.worker.progress.emit((freqs, data))


class DashboardInstr:
    def __init__(self, par):
        self.__par = par

        self.center = None
        self.span = None
        self.min = None
        self.max = None
        self.sweep = None
        self.slices = {}
        self.instr = None  # set to True in debug mode to baypass every control

        self.worker = Worker()
        self.worker.set_parent(self)
        self.worker.progress.connect(lambda t: self.__update_spec(t))

        self.__hide = False
        self.__thread = QThread()
        self.__thread.started.connect(self.worker.run)
        self.worker.moveToThread(self.__thread)
        self.__thread.start()

        self.__canvas = MplSpecCanvas()
        self.__par.ui.verticalLayoutSpecInstr.addWidget(self.__canvas.get_toolbar())
        self.__par.ui.verticalLayoutSpecInstr.addWidget(self.__canvas)
        self.__enable_disable(False)

        set_icon(self.__par.ui.pushButtonConnect, i_name.ADD_LINK, globals.theme, True)
        set_icon(
            self.__par.ui.pushButtonSaveData,
            i_name.FILE_SAVE,
            globals.theme,
            True,
        )
        set_icon(
            self.__par.ui.pushButtonHide,
            i_name.VISIBILITY if self.__hide else i_name.VISIBILITY_OFF,
            globals.theme,
            True,
        )
        set_icon(
            self.__par.ui.pushButtonClear,
            i_name.CLEANING_SERVICE,
            globals.theme,
            True,
        )

        set_icon(
            self.__par.ui.pushButtonSavePreset,
            i_name.FILE_SAVE,
            globals.theme,
            True,
        )

        set_icon(
            self.__par.ui.labelCenter,
            i_name.ADJUST,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelSpan,
            i_name.ARROW_RANGE,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelMin,
            i_name.ARROW_MENU_CLOSE,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelMax,
            i_name.ARROW_MENU_OPEN,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelOffsetsInstr,
            i_name.CADENCE,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelSweep,
            i_name.AV_TIMER,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelStartTime,
            i_name.TIMER_PLAY,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelDuration,
            i_name.HOURGLASS,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelSlices,
            i_name.LOCAL_PIZZA,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__par.ui.labelPresets,
            i_name.DISPLAY_SETTINGS,
            globals.theme,
            True,
            (30, 30),
        )

        set_icon(self.__par.ui.pushButtonApply1, i_name.CHECK, globals.theme, True)
        set_icon(self.__par.ui.pushButtonApply2, i_name.CHECK, globals.theme, True)
        set_icon(self.__par.ui.pushButtonApply3, i_name.CHECK, globals.theme, True)

        self.__par.ui.doubleSpinBoxCenter.editingFinished.connect(self.__apply_cs)
        self.__par.ui.doubleSpinBoxSpan.editingFinished.connect(self.__apply_cs)
        self.__par.ui.doubleSpinBoxMin.editingFinished.connect(self.__apply_mm)
        self.__par.ui.doubleSpinBoxMax.editingFinished.connect(self.__apply_mm)
        self.__par.ui.doubleSpinBoxSweep.editingFinished.connect(self.__apply_s)

        self.__par.ui.pushButtonApply1.clicked.connect(self.__apply_cs)
        self.__par.ui.pushButtonApply2.clicked.connect(self.__apply_mm)
        self.__par.ui.pushButtonApply3.clicked.connect(self.__apply_s)

        self.__par.ui.pushButtonConnect.clicked.connect(self.__conn_disconn)
        self.__par.ui.pushButtonSaveData.clicked.connect(self.__save_data)
        self.__par.ui.pushButtonHide.clicked.connect(self.__invert_hide)
        self.__par.ui.pushButtonClear.clicked.connect(lambda x: self.slices.clear())
        self.__par.ui.comboBoxPresets.currentIndexChanged.connect(
            self.__comboBoxPresetsCurrentIndexChanged
        )
        self.__par.ui.comboBoxOffsetsInstr.addItems(self.__par.bands)
        self.__par.ui.comboBoxOffsetsInstr.currentIndexChanged.connect(
            self.__comboBoxOffsetsInstrCurrentIndexChanged
        )

        if "controller" in self.__par.args:
            if "presets" in self.__par.args["controller"]:
                self.__presets = self.__par.args["controller"]["presets"]
                presets = list(map(lambda x: x["name"], self.__presets))
                self.__par.ui.comboBoxPresets.addItems(presets)

    def __apply_cs(self):
        center = self.__par.ui.doubleSpinBoxCenter.value()
        span = self.__par.ui.doubleSpinBoxSpan.value()
        if center == self.center and span == self.span:
            return

        self.thread_safe = False
        self.slices.clear()
        self.center = center
        self.span = span
        self.min = self.center - self.span
        self.max = self.center + self.span
        self.instr.write_str(f"SENS:FREQ:CENT {self.center}")
        self.instr.write_str(f"SENS:FREQ:SPAN {self.span}")
        self.__par.ui.doubleSpinBoxMin.setValue(self.min)
        self.__par.ui.doubleSpinBoxMax.setValue(self.max)
        self.thread_safe = True

    def __apply_mm(self):
        min = self.__par.ui.doubleSpinBoxMin.value()
        max = self.__par.ui.doubleSpinBoxMax.value()
        if min == self.min and max == self.max:
            return

        self.thread_safe = False
        self.slices.clear()
        self.min = min
        self.max = max
        self.center = (self.min + self.max) / 2
        self.span = self.center - self.min
        self.instr.write_str(f"SENS:FREQ:CENT {self.center}")
        self.instr.write_str(f"SENS:FREQ:SPAN {self.span}")
        self.__par.ui.doubleSpinBoxCenter.setValue(self.center)
        self.__par.ui.doubleSpinBoxSpan.setValue(self.span)
        self.thread_safe = True

    def __apply_s(self):
        sweep = self.__par.ui.doubleSpinBoxSweep.value()
        if sweep == self.sweep:
            return

        self.thread_safe = False
        self.sweep = sweep
        self.instr.write_str(f"SENS:SWE:TIME {self.sweep}")
        self.thread_safe = True

    def __invert_hide(self):
        self.__hide = not self.__hide
        set_icon(
            self.__par.ui.pushButtonHide,
            i_name.VISIBILITY if self.__hide else i_name.VISIBILITY_OFF,
            globals.theme,
            True,
        )
        if self.__hide:
            self.__canvas.axes.text(
                0.45,
                1.01,
                "Hidden from the user!",
                transform=self.__canvas.axes.transAxes,
            )
        else:
            for txt in self.__canvas.axes.texts:
                txt.remove()

        self.__canvas.draw()

    def __save_data(self):
        print("__save_data not implemented")

    def __comboBoxPresetsCurrentIndexChanged(self, d):
        preset = self.__presets[d]
        self.min = None
        self.max = None
        self.center = None
        self.span = None
        self.sweep = None
        if "min" in preset and "max" in preset:
            self.min = preset["min"]
            self.max = preset["max"]
            self.center = (self.max - self.min) / 2
            self.span = self.max - self.center
        elif "center" in preset and "span" in preset:
            self.center = preset["center"]
            self.span = preset["snap"]
            self.min = self.center - self.span
            self.max = self.center + self.span

        if "sweep" in preset:
            self.sweep = preset["sweep"]

        self.__par.ui.doubleSpinBoxCenter.setValue(self.center)
        self.__par.ui.doubleSpinBoxSpan.setValue(self.span)
        self.__par.ui.doubleSpinBoxMin.setValue(self.min)
        self.__par.ui.doubleSpinBoxMax.setValue(self.max)
        self.__par.ui.doubleSpinBoxSweep.setValue(self.sweep)

    def __comboBoxOffsetsInstrCurrentIndexChanged(self, d):
        self.__lo = self.__par.args["lo"][d]["value"]

    def __disconnect_instr(self):
        self.instr.close()
        self.instr = None
        self.slices.clear()
        self.__enable_disable(False)

        args = {}
        args["text"] = f"Successful disconnection"
        args["image"] = get_icon_path(i_name.CHECK, globals.theme)
        WindowManager(UIPopupDialog, UXPopupDialog, args, self.__par.dialog).show()

    def __connect_instr(self, key: str):
        try:
            self.thread_safe = False

            self.instr = RsInstrument(key, id_query=True, reset=True)
            self.instr.write_str("SYST:BEEP:KEY:VOL 0")
            self.instr.write_str("SYST:BEEP:POV ON")
            self.instr.write_str("SYST:BEEP:VOL 1")
            self.instr.write_str("SYST:DISP:UPD ON")
            n = datetime.now()
            self.instr.write_str(f"SYST:DATE {n.year},{n.month},{n.day}")
            self.instr.write_str(f"SYST:TIME {n.hour},{n.minute},{n.second}")
            self.instr.write_str("SYST:TZON 01,00")
            self.instr.write_str("UNIT:LENG MET")
            self.instr.write_str("INST:SEL SAN")
            self.instr.write_str("UNIT:POW W")
            self.instr.write_str("INIT:CONT OFF")
            self.instr.write_str(f"SENS:FREQ:CENT {self.center}")
            self.instr.write_str(f"SENS:FREQ:SPAN {self.span}")
            self.instr.write_str(f"SENS:SWE:TIME {self.sweep}")

            self.thread_safe = True

            self.__par.ui.lineEditResourceName.setText(self.instr.resource_name)
            self.__par.ui.lineEditManufacturer.setText(self.instr.manufacturer)
            self.__par.ui.lineEditModelName.setText(
                self.instr.full_instrument_model_name
            )
            self.__par.ui.lineEditSerialNumber.setText(
                self.instr.instrument_serial_number
            )
            self.__par.ui.lineEditFW.setText(self.instr.instrument_firmware_version)
            self.__par.ui.lineEditDriver.setText(self.instr.driver_version)
            self.__par.ui.lineEditVisa.setText(self.instr.visa_manufacturer)
            self.__par.ui.lineEditName.setText(self.instr.full_instrument_model_name)
            self.__par.ui.lineEditOptions.setText(
                ",".join(self.instr.instrument_options)
            )
            self.__enable_disable(True)

            args = {}
            args["text"] = f"Connected!"
            args["image"] = get_icon_path(i_name.CHECK, globals.theme)
            WindowManager(UIPopupDialog, UXPopupDialog, args, self.__par.dialog).show()
        except:
            MessageBox(
                text=f"Error during connection device {key}:\n{traceback.format_exc()}",
                title="WOW",
                icon=QMessageBox.Icon.Critical,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()

    def __conn_disconn(self):
        if self.instr and self.instr.is_connection_active:
            self.__disconnect_instr()
            return

        try:
            instr_list = RsInstrument.list_resources("?*")
            if instr_list:
                key = None
                if (
                    "controller" in self.__par.args
                    and "instrument" in self.__par.args["controller"]
                    and self.__par.args["controller"]["instrument"] in instr_list
                ):
                    key = self.__par.args["controller"]["instrument"]
                elif len(instr_list) == 1:
                    key = instr_list[0]
                    if (
                        MessageBox(
                            text=f"Connect to {key}? It is the only instrument available.",
                            title="WOW",
                            icon=QMessageBox.Icon.Question,
                            buttons=QMessageBox.StandardButton.Yes
                            | QMessageBox.StandardButton.No,
                        ).result()
                        == QMessageBox.StandardButton.No
                    ):
                        return
                else:
                    win = WindowManager(
                        UIComboBoxDialog,
                        UXComboBoxDialog,
                        instr_list,
                        self.__par.dialog,
                    )
                    win.exec()
                    key = win.bh.text

                self.__connect_instr(key)
            else:
                args = {}
                args["text"] = f"No instrument available"
                args["image"] = get_icon_path(i_name.INFO, globals.theme)
                WindowManager(
                    UIPopupDialog, UXPopupDialog, args, self.__par.dialog
                ).show()
        except:
            MessageBox(
                text=f"Error during searching devices:\n{traceback.format_exc()}",
                title="WOW",
                icon=QMessageBox.Icon.Critical,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()

    @Slot(tuple)
    def __update_spec(self, t):
        self.slices[datetime.now(timezone.utc)] = (t[0], t[1])

        spec = {
            "r": list(map(lambda x: x.timestamp(), self.slices.keys())),
            "f": list(map(lambda x: float(x), t[0])),
            "m": np.array(list(self.slices.values())).astype(float)[:, 1, :][-10:],
        }

        if not self.__hide:
            self.__canvas.set_data(spec, self.__par.args["viewer"])

        if self.slices:
            msg = list(self.slices)[0].strftime("%H:%M:%S %d-%m-%Y")
            self.__par.ui.lineEditStartTime.setText(msg)
            msg = (datetime.now(timezone.utc) - list(self.slices)[0]).total_seconds()
            self.__par.ui.lineEditDuration.setText(str(int(msg)))
            self.__par.ui.lineEditSlices.setText(str(len(self.slices)))

    def __enable_disable(self, enable):
        if enable:
            set_icon(
                self.__par.ui.pushButtonConnect,
                i_name.LINK_OFF,
                globals.theme,
                True,
            )
        else:
            set_icon(
                self.__par.ui.pushButtonConnect,
                i_name.ADD_LINK,
                globals.theme,
                True,
            )
            self.__par.ui.lineEditResourceName.setText("---")
            self.__par.ui.lineEditManufacturer.setText("---")
            self.__par.ui.lineEditModelName.setText("---")
            self.__par.ui.lineEditSerialNumber.setText("---")
            self.__par.ui.lineEditFW.setText("---")
            self.__par.ui.lineEditDriver.setText("---")
            self.__par.ui.lineEditVisa.setText("---")
            self.__par.ui.lineEditName.setText("---")
            self.__par.ui.lineEditOptions.setText("---")

        self.__par.ui.labelCenter.setEnabled(enable)
        self.__par.ui.doubleSpinBoxCenter.setEnabled(enable)
        self.__par.ui.labelSpan.setEnabled(enable)
        self.__par.ui.doubleSpinBoxSpan.setEnabled(enable)
        self.__par.ui.labelMin.setEnabled(enable)
        self.__par.ui.doubleSpinBoxMin.setEnabled(enable)
        self.__par.ui.labelMax.setEnabled(enable)
        self.__par.ui.doubleSpinBoxMax.setEnabled(enable)
        self.__par.ui.labelSweep.setEnabled(enable)
        self.__par.ui.doubleSpinBoxSweep.setEnabled(enable)
        self.__par.ui.labelOffsetsInstr.setEnabled(enable)
        self.__par.ui.comboBoxOffsetsInstr.setEnabled(enable)
