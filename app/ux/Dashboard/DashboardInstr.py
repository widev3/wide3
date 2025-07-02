import random
import globals
import numpy as np
from despyner.MessageBox import MessageBox
from ux.MplSpecCanvas import MplSpecCanvas
from despyner.QtMger import set_icon, icon_name
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
from despyner.QtMger import set_icon, icon_name, WindowManager, get_icon_path
from despyner.comboBoxDialog.ComboBoxDialog import Ui_Dialog as UIComboBoxDialog


class Worker(QObject):
    progress = Signal(tuple)

    def set_parent(self, parent):
        self.__parent = parent

    def run(self):
        while True:
            time.sleep(5)
            while self.__parent.instr:
                is_instr = isinstance(self.__parent.instr, RsInstrument)
                if is_instr and self.__parent.instr:
                    self.__parent.instr.write_str("INIT:IMM")

                time.sleep(self.__parent.sweep + 1)

                data = []
                if is_instr:
                    if self.__parent.instr:
                        data = self.__parent.instr.query_str_list("TRACE:DATA?")
                    else:
                        continue
                else:
                    data = [random.random() for _ in range(1000)]

                if data:
                    start = self.__parent.center - self.__parent.span
                    stop = self.__parent.center + self.__parent.span
                    freqs = list(map(lambda x: x, np.linspace(start, stop, len(data))))
                    self.__parent.worker.progress.emit((freqs, data))


class DashboardInstr:
    def __init__(self, parent):
        self.__parent = parent

        self.center = 10
        self.span = 5
        self.sweep = 1
        self.slices = {}
        self.hide = False

        self.worker = Worker()
        self.worker.set_parent(self)
        self.worker.progress.connect(lambda t: self.__update_spec(t))

        self.thread = QThread()
        self.thread.started.connect(self.worker.run)
        self.worker.moveToThread(self.thread)
        self.thread.start()

        self.__canvas = MplSpecCanvas()
        self.__parent.ui.verticalLayoutSpecInstr.addWidget(self.__canvas.get_toolbar())
        self.__parent.ui.verticalLayoutSpecInstr.addWidget(self.__canvas)

        self.instr = None  # set to True in debug mode to baypass every control
        self.__enable_disable(False)

        set_icon(
            self.__parent.ui.pushButtonConnect, icon_name.ADD_LINK, globals.theme, True
        )
        set_icon(
            self.__parent.ui.pushButtonSaveData,
            icon_name.FILE_SAVE,
            globals.theme,
            True,
        )
        set_icon(
            self.__parent.ui.pushButtonHide,
            icon_name.VISIBILITY if self.hide else icon_name.VISIBILITY_OFF,
            globals.theme,
            True,
        )
        set_icon(
            self.__parent.ui.pushButtonClear,
            icon_name.CLEANING_SERVICE,
            globals.theme,
            True,
        )

        set_icon(
            self.__parent.ui.pushButtonSavePreset,
            icon_name.FILE_SAVE,
            globals.theme,
            True,
        )

        set_icon(
            self.__parent.ui.labelCenter,
            icon_name.ADJUST,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelSpan,
            icon_name.ARROW_RANGE,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelMin,
            icon_name.ARROW_MENU_CLOSE,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelMax,
            icon_name.ARROW_MENU_OPEN,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelOffsetsInstr,
            icon_name.CADENCE,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelSweep,
            icon_name.AV_TIMER,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelStartTime,
            icon_name.TIMER_PLAY,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelDuration,
            icon_name.HOURGLASS,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelSlices,
            icon_name.LOCAL_PIZZA,
            globals.theme,
            True,
            (30, 30),
        )
        set_icon(
            self.__parent.ui.labelPresets,
            icon_name.DISPLAY_SETTINGS,
            globals.theme,
            True,
            (30, 30),
        )

        self.__parent.ui.doubleSpinBoxCenter.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxSpan.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxMin.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxMax.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxSweep.valueChanged.connect(lambda x: None)
        self.__parent.ui.pushButtonConnect.clicked.connect(self.__conn_disconn)
        self.__parent.ui.pushButtonSaveData.clicked.connect(self.__save_data)
        self.__parent.ui.pushButtonHide.clicked.connect(self.__invert_hide)
        self.__parent.ui.pushButtonClear.clicked.connect(lambda x: self.slices.clear())
        self.__parent.ui.comboBoxOffsetsInstr.addItems(self.__parent.bands)
        self.__parent.ui.comboBoxOffsetsInstr.currentIndexChanged.connect(
            self.__comboBoxOffsetsInstrCurrentIndexChanged
        )

    def __invert_hide(self):
        self.hide = not self.hide
        set_icon(
            self.__parent.ui.pushButtonHide,
            icon_name.VISIBILITY if self.hide else icon_name.VISIBILITY_OFF,
            globals.theme,
            True,
        )
        if self.hide:
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

    def __comboBoxOffsetsInstrCurrentIndexChanged(self, d):
        self.__lo = self.__parent.args["lo"][d]["value"]

    def __disconnect_instr(self):
        self.instr.close()
        self.instr = None
        self.slices.clear()
        self.__enable_disable(False)
        self.__parent.ui.lineEditIDN.setText("---")
        self.__parent.ui.lineEditDriver.setText("---")
        self.__parent.ui.lineEditVisa.setText("---")
        self.__parent.ui.lineEditName.setText("---")
        self.__parent.ui.lineEditOptions.setText("---")

        args = {}
        args["text"] = f"Successful disconnection"
        args["image"] = get_icon_path(icon_name.CHECK, globals.theme)
        WindowManager(UIPopupDialog, UXPopupDialog, args).show()

    def __connect_instr(self, key: str):
        try:
            self.instr = RsInstrument(key, id_query=True, reset=True)

            n = datetime.now()
            self.instr.write_str("SYST:BEEP:KEY:VOL 0")
            self.instr.write_str("SYST:BEEP:POV ON")
            self.instr.write_str("SYST:BEEP:VOL 1")
            self.instr.write_str("SYST:DISP:UPD ON")
            self.instr.write_str(f"SYST:DATE {n.year},{n.month},{n.day}")
            self.instr.write_str(f"SYST:TIME {n.hour},{n.minute},{n.second}")
            self.instr.write_str("SYST:TZON 01,00")
            self.instr.write_str("UNIT:LENG MET")
            self.instr.write_str("INST:SEL SAN")
            self.instr.write_str("UNIT:POW W")
            self.instr.write_str("INIT:CONT OFF")

            if "controller" in self.__parent.args:
                if "center" in self.__parent.args["controller"]:
                    self.center = self.__parent.args["controller"]["center"]
                    self.instr.write_str(f"SENS:FREQ:CENT {self.center}")
                    self.__parent.ui.doubleSpinBoxCenter.setValue(self.center)

            if "controller" in self.__parent.args:
                if "span" in self.__parent.args["controller"]:
                    self.span = self.__parent.args["controller"]["span"]
                    self.instr.write_str(f"SENS:FREQ:SPAN {self.span}")
                    self.__parent.ui.doubleSpinBoxSpan.setValue(self.span)

            if "controller" in self.__parent.args:
                if "sweep" in self.__parent.args["controller"]:
                    self.sweep = self.__parent.args["controller"]["sweep"]
                    self.instr.write_str(f"SENS:SWE:TIME {self.sweep}")
                    self.__parent.ui.doubleSpinBoxSweep.setValue(self.sweep)

            self.__parent.ui.doubleSpinBoxMin.setValue(self.center - self.span)
            self.__parent.ui.doubleSpinBoxMax.setValue(self.center + self.span)

            self.__parent.ui.lineEditResourceName.setText(self.instr.resource_name)
            self.__parent.ui.lineEditManufacturer.setText(self.instr.manufacturer)
            self.__parent.ui.lineEditModelName.setText(
                self.instr.full_instrument_model_name
            )
            self.__parent.ui.lineEditSerialNumber.setText(
                self.instr.instrument_serial_number
            )
            self.__parent.ui.lineEditFW.setText(self.instr.instrument_firmware_version)
            self.__parent.ui.lineEditDriver.setText(self.instr.driver_version)
            self.__parent.ui.lineEditVisa.setText(self.instr.visa_manufacturer)
            self.__parent.ui.lineEditName.setText(self.instr.full_instrument_model_name)
            self.__parent.ui.lineEditOptions.setText(
                ",".join(self.instr.instrument_options)
            )
            self.__enable_disable(True)

            args = {}
            args["text"] = f"Connected!"
            args["image"] = get_icon_path(icon_name.CHECK, globals.theme)
            WindowManager(UIPopupDialog, UXPopupDialog, args).show()
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
                    "controller" in self.__parent.args
                    and "instrument" in self.__parent.args["controller"]
                    and self.__parent.args["controller"]["instrument"] in instr_list
                ):
                    key = self.__parent.args["controller"]["instrument"]
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
                    win = WindowManager(UIComboBoxDialog, UXComboBoxDialog, instr_list)
                    win.exec()
                    key = win.bh.text

                self.__connect_instr(key)
            else:
                args = {}
                args["text"] = f"No instrument available"
                args["image"] = get_icon_path(icon_name.INFO, globals.theme)
                WindowManager(UIPopupDialog, UXPopupDialog, args).show()
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
            "m": np.rot90(np.array(list(self.slices.values())).astype(float)[:, 1, :]),
        }

        if not self.hide:
            self.__canvas.set_data(spec, self.__parent.args["viewer"])

        msg = list(self.slices)[0].strftime("%H:%M:%S %d-%m-%Y")
        self.__parent.ui.lineEditStartTime.setText(msg)

        msg = (datetime.now(timezone.utc) - list(self.slices)[0]).total_seconds()
        self.__parent.ui.lineEditDuration.setText(str(int(msg)))

        self.__parent.ui.lineEditSlices.setText(str(len(self.slices)))

    def __enable_disable(self, enable):
        if enable:
            set_icon(
                self.__parent.ui.pushButtonConnect,
                icon_name.LINK_OFF,
                globals.theme,
                True,
            )
        else:
            set_icon(
                self.__parent.ui.pushButtonConnect,
                icon_name.ADD_LINK,
                globals.theme,
                True,
            )

        self.__parent.ui.labelCenter.setEnabled(enable)
        self.__parent.ui.doubleSpinBoxCenter.setEnabled(enable)
        self.__parent.ui.labelSpan.setEnabled(enable)
        self.__parent.ui.doubleSpinBoxSpan.setEnabled(enable)
        self.__parent.ui.labelMin.setEnabled(enable)
        self.__parent.ui.doubleSpinBoxMin.setEnabled(enable)
        self.__parent.ui.labelMax.setEnabled(enable)
        self.__parent.ui.doubleSpinBoxMax.setEnabled(enable)
        self.__parent.ui.labelSweep.setEnabled(enable)
        self.__parent.ui.doubleSpinBoxSweep.setEnabled(enable)
        self.__parent.ui.labelOffsetsInstr.setEnabled(enable)
        self.__parent.ui.comboBoxOffsetsInstr.setEnabled(enable)
