import random
import numpy as np
from kernel.MessageBox import MessageBox
from ux.MplSpecCanvas import MplSpecCanvas
from kernel.QtMger import set_icon, icon_types
from kernel.popupDialog.UXPopupDialog import UXPopupDialog
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
from kernel.comboBoxDialog.UXComboBoxDialog import UXComboBoxDialog
from kernel.popupDialog.PopupDialog import Ui_Dialog as UIPopupDialog
from kernel.QtMger import set_icon, icon_types, WindowManager, get_icon_path
from kernel.comboBoxDialog.ComboBoxDialog import Ui_Dialog as UIComboBoxDialog


class Worker(QObject):
    progress = Signal(tuple)

    def set_parent(self, parent):
        self.__parent = parent

    def run(self):
        while True:
            time.sleep(5)
            while self.__parent:
                is_instr = isinstance(self.__parent.instr, RsInstrument)
                if is_instr:
                    self.__parent.instr.write_str("INIT:IMM")

                time.sleep(self.__parent.sweep + 1)

                data = []
                if is_instr:
                    data = self.__parent.instr.query_str_list("TRACE:DATA?")
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

        set_icon(self.__parent.ui.pushButtonConnect, icon_types.ADD_LINK)
        set_icon(self.__parent.ui.pushButtonRecord, icon_types.CAMERA)
        set_icon(self.__parent.ui.labelCenter, icon_types.ADJUST, (30, 30))
        set_icon(self.__parent.ui.labelSpan, icon_types.ARROW_RANGE, (30, 30))
        set_icon(self.__parent.ui.labelMin, icon_types.ARROW_MENU_CLOSE, (30, 30))
        set_icon(self.__parent.ui.labelMax, icon_types.ARROW_MENU_OPEN, (30, 30))
        set_icon(self.__parent.ui.labelOffsetsInstr, icon_types.CADENCE, (30, 30))
        set_icon(self.__parent.ui.labelSweep, icon_types.AV_TIMER, (30, 30))
        set_icon(self.__parent.ui.labelStartTime, icon_types.HOURGLASS, (30, 30))
        set_icon(self.__parent.ui.labelSlices, icon_types.LOCAL_PIZZA, (30, 30))

        self.__parent.ui.doubleSpinBoxCenter.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxSpan.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxMin.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxMax.valueChanged.connect(lambda x: None)
        self.__parent.ui.doubleSpinBoxSweep.valueChanged.connect(lambda x: None)
        self.__parent.ui.pushButtonConnect.clicked.connect(self.__conn_disconn)
        self.__parent.ui.pushButtonRecord.clicked.connect(self.__record)
        self.__parent.ui.comboBoxOffsetsInstr.addItems(self.__parent.bands)

        self.record = False
        self.center = 10
        self.span = 5
        self.sweep = 1
        self.slices = {}

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

        self.instr = True  # comment this line
        # self.__enable_disable(False) # uncomment this line

    def __conn_disconn(self):
        def __disconnect_instr(self):
            self.__parent.instr.close()
            self.__parent.instr = None

            self.__parent.__enable_disable(False)
            self.__parent.ui.labelIDN.setText("---")
            self.__parent.ui.labelDriver.setText("---")
            self.__parent.ui.labelVISA.setText("---")
            self.__parent.ui.labelName.setText("---")
            self.__parent.ui.labelOptions.setText("---")

            args = {}
            args["text"] = f"Successful disconnection"
            args["image"] = get_icon_path(icon_types.INFO)
            WindowManager(UIPopupDialog, UXPopupDialog, args).show()

        def __connect_instr(self, key: str):
            try:
                self.__parent.instr = RsInstrument(key, id_query=True, reset=True)

                n = datetime.now()
                self.__parent.instr.write_str("SYST:BEEP:KEY:VOL 0")
                self.__parent.instr.write_str("SYST:BEEP:POV ON")
                self.__parent.instr.write_str("SYST:BEEP:VOL 1")
                self.__parent.instr.write_str("SYST:DISP:UPD ON")
                self.__parent.instr.write_str(f"SYST:DATE {n.year},{n.month},{n.day}")
                self.__parent.instr.write_str(
                    f"SYST:TIME {n.hour},{n.minute},{n.second}"
                )
                self.__parent.instr.write_str("SYST:TZON 01,00")
                self.__parent.instr.write_str("UNIT:LENG MET")
                self.__parent.instr.write_str("INST:SEL SAN")
                self.__parent.instr.write_str("UNIT:POW W")
                self.__parent.instr.write_str("INIT:CONT OFF")
                if (
                    "controller" in self.__parent.args
                    and "center" in self.__parent.args["controller"]
                ):
                    self.__parent.center = self.__parent.args["controller"]["center"]
                    self.__parent.instr.write_str(
                        f"SENS:FREQ:CENT {self.__parent.center}"
                    )
                    self.__parent.ui.doubleSpinBoxCenter.setValue(self.__parent.center)
                if (
                    "controller" in self.__parent.args
                    and "span" in self.__parent.args["controller"]
                ):
                    self.__parent.span = self.__parent.args["controller"]["span"]
                    self.__parent.instr.write_str(
                        f"SENS:FREQ:SPAN {self.__parent.span}"
                    )
                    self.__parent.ui.doubleSpinBoxSpan.setValue(self.__parent.span)
                if (
                    "controller" in self.__parent.args
                    and "sweep" in self.__parent.args["controller"]
                ):
                    self.__parent.sweep = self.__parent.args["controller"]["sweep"]
                    self.__parent.instr.write_str(
                        f"SENS:SWE:TIME {self.__parent.sweep}"
                    )
                    self.__parent.ui.doubleSpinBoxSweep.setValue(self.__parent.sweep)

                self.__parent.ui.doubleSpinBoxMin.setValue(
                    self.__parent.center - self.__parent.span
                )
                self.__parent.ui.doubleSpinBoxMax.setValue(
                    self.__parent.center + self.__parent.span
                )

                idn = self.__parent.instr.query_str("*IDN?")
                self.__parent.ui.lineEditIDN.setText(idn)
                self.__parent.ui.lineEditDriver.setText(
                    self.__parent.instr.driver_version
                )
                self.__parent.ui.lineEditVisa.setText(
                    self.__parent.instr.visa_manufacturer
                )
                self.__parent.ui.lineEditName.setText(
                    self.__parent.instr.full_instrument_model_name
                )
                self.__parent.ui.lineEditOptions.setText(
                    ",".join(self.__parent.instr.instrument_options)
                )
                self.__enable_disable(True)

                args = {}
                args["text"] = f"Connected!"
                args["image"] = get_icon_path(icon_types.CHECK)
                WindowManager(UIPopupDialog, UXPopupDialog, args).show()
            except:
                MessageBox(
                    text=f"Error during connection device {key}:\n{traceback.format_exc()}",
                    title="WOW",
                    icon=QMessageBox.Icon.Critical,
                    buttons=QMessageBox.StandardButton.Ok,
                ).result()

        if self.__parent.instr and self.__parent.instr.is_connection_active:
            __disconnect_instr(self.__parent)
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

                __connect_instr(self.__parent, key)
            else:
                args = {}
                args["text"] = f"No instrument available"
                args["image"] = get_icon_path(icon_types.INFO)
                WindowManager(UIPopupDialog, UXPopupDialog, args).show()
        except:
            MessageBox(
                text=f"Error during searching devices:\n{traceback.format_exc()}",
                title="WOW",
                icon=QMessageBox.Icon.Critical,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()

    def __record(self):
        self.record = not self.record

    @Slot(tuple)
    def __update_spec(self, t):
        self.slices[datetime.now(timezone.utc)] = (t[0], t[1])

        spec = {
            "r": list(map(lambda x: x.timestamp(), self.slices.keys())),
            "f": t[0],
            "m": list(
                zip(*list(map(lambda x: x[1], list(self.slices.values())[::-1]))[::-1])
            ),
        }
        self.__canvas.set_data(spec, self.__parent.args["viewer"])
        msg = f"{list(self.slices)[0].strftime("%H:%M:%S %d-%m-%Y")} ({(datetime.now(timezone.utc)-list(self.slices)[0]).total_seconds()} s)"
        self.__parent.ui.lineEditStartTime.setText(msg)
        self.__parent.ui.lineEditSlices.setText(str(len(self.slices)))

    def __enable_disable(self, enable):
        if enable:
            set_icon(self.__parent.ui.pushButtonConnect, icon_types.LINK_OFF)
        else:
            set_icon(self.__parent.ui.pushButtonConnect, icon_types.ADD_LINK)

        self.__parent.ui.pushButtonRecord.setEnabled(enable)
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
