import time
import threading
import numpy as np
from kernel.MessageBox import MessageBox
from ux.MplSpecCanvas import MplSpecCanvas
from single_include import QMessageBox, QApplication
from kernel.QtMger import set_icon, icon_types
from kernel.popupDialog.UXPopupDialog import UXPopupDialog
from single_include import RsInstrument, traceback, datetime
from kernel.comboBoxDialog.UXComboBoxDialog import UXComboBoxDialog
from kernel.popupDialog.PopupDialog import Ui_Dialog as UIPopupDialog
from kernel.QtMger import set_icon, icon_types, WindowManager, get_icon_path
from kernel.comboBoxDialog.ComboBoxDialog import Ui_Dialog as UIComboBoxDialog


def init(self):
    set_icon(self.ui.pushButtonConnect, icon_types.ADD_LINK)
    set_icon(self.ui.pushButtonRecord, icon_types.CAMERA)
    set_icon(self.ui.labelCenter, icon_types.ADJUST, (30, 30))
    set_icon(self.ui.labelSpan, icon_types.ARROW_RANGE, (30, 30))
    set_icon(self.ui.labelMin, icon_types.ARROW_MENU_CLOSE, (30, 30))
    set_icon(self.ui.labelMax, icon_types.ARROW_MENU_OPEN, (30, 30))
    set_icon(self.ui.labelOffsetsInstr, icon_types.CADENCE, (30, 30))
    set_icon(self.ui.labelSweep, icon_types.AV_TIMER, (30, 30))
    set_icon(self.ui.labelStartTime, icon_types.HOURGLASS, (30, 30))
    set_icon(self.ui.labelSlices, icon_types.LOCAL_PIZZA, (30, 30))

    self.ui.doubleSpinBoxCenter.valueChanged.connect(lambda x: None)
    self.ui.doubleSpinBoxSpan.valueChanged.connect(lambda x: None)
    self.ui.doubleSpinBoxMin.valueChanged.connect(lambda x: None)
    self.ui.doubleSpinBoxMax.valueChanged.connect(lambda x: None)
    self.ui.doubleSpinBoxSweep.valueChanged.connect(lambda x: None)

    self.ui.pushButtonConnect.clicked.connect(lambda: __conn_disconn(self))
    self.ui.pushButtonLive.clicked.connect(lambda: __live(self))
    self.ui.pushButtonRecord.clicked.connect(lambda: __record(self))

    self.__record = False
    self.__slices_queue = []
    self.__thread_instr = threading.Thread(target=lambda: __record_thread(self))
    self.__thread_instr.daemon = True
    self.__thread_instr.start()

    bands = list(map(lambda x: f"{x["band"]}: {x["value"]}", self.args["lo"]))
    self.ui.comboBoxOffsetsInstr.addItems(bands)
    __enable_disable(self, False)
    self.__block_signal = False


def __conn_disconn(self):
    def __disconnect_instr(self):
        self.instr.close()
        self.instr = None

        self.__enable_disable(False)
        self.ui.labelIDN.setText("---")
        self.ui.labelDriver.setText("---")
        self.ui.labelVISA.setText("---")
        self.ui.labelName.setText("---")
        self.ui.labelOptions.setText("---")

        args = {}
        args["text"] = f"Successful disconnection"
        args["image"] = get_icon_path(icon_types.INFO)
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
            self.instr.write_str("INIT:CONT ON")
            if "controller" in self.args and "center" in self.args["controller"]:
                self.__center = self.args["controller"]["center"]
                self.instr.write_str(f"SENS:FREQ:CENT {self.__center}")
                self.ui.doubleSpinBoxCenter.setValue(self.__center)
            if "controller" in self.args and "span" in self.args["controller"]:
                self.__span = self.args["controller"]["span"]
                self.instr.write_str(f"SENS:FREQ:SPAN {self.__span}")
                self.ui.doubleSpinBoxSpan.setValue(self.__span)
            if "controller" in self.args and "sweep" in self.args["controller"]:
                self.__sweep = self.args["controller"]["sweep"]
                self.instr.write_str(f"SENS:SWE:TIME {self.__sweep}")
                self.ui.doubleSpinBoxSweep.setValue(self.__sweep)

            self.ui.doubleSpinBoxMin.setValue(self.__center - self.__span)
            self.ui.doubleSpinBoxMax.setValue(self.__center + self.__span)

            idn = self.instr.query_str("*IDN?")
            self.ui.lineEditIDN.setText(idn)
            self.ui.lineEditDriver.setText(self.instr.driver_version)
            self.ui.lineEditVisa.setText(self.instr.visa_manufacturer)
            self.ui.lineEditName.setText(self.instr.full_instrument_model_name)
            self.ui.lineEditOptions.setText(",".join(self.instr.instrument_options))
            __enable_disable(self, True)

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

    if self.instr and self.instr.is_connection_active:
        __disconnect_instr(self)
        return

    try:
        instr_list = RsInstrument.list_resources("?*")

        if instr_list:
            key = None
            if (
                "controller" in self.args
                and "instrument" in self.args["controller"]
                and self.args["controller"]["instrument"] in instr_list
            ):
                key = self.args["controller"]["instrument"]
            elif len(instr_list) == 1:
                key = instr_list[0]
                res = MessageBox(
                    text=f"Connect to {key}? It is the only instrument available.",
                    title="WOW",
                    icon=QMessageBox.Icon.Question,
                    buttons=QMessageBox.StandardButton.Yes
                    | QMessageBox.StandardButton.No,
                ).result()
                if res == QMessageBox.StandardButton.No:
                    return
            else:
                win = WindowManager(UIComboBoxDialog, UXComboBoxDialog, instr_list)
                win.exec()
                key = win.bh.text

            __connect_instr(self, key)
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


def __live(self):
    self.__live = not self.__live


def __record(self):
    self.__record = not self.__record


def __record_thread(self):
    last_record = None
    while True:
        time.sleep(1)
        if not self.instr:
            continue

        if not self.__live and self.__slices_queue:
            print(self.__slices_queue)
            self.__slices_queue = []

        if last_record != self.__live:
            last_record = self.__live
            if self.__live:
                self.instr.write_str("INIT:CONT OFF")
                self.__slices_queue = []
            else:
                self.instr.write_str("INIT:CONT ON")

        if self.__live:
            self.instr.write_str("INIT:IMM")
            time.sleep(self.__sweep + 1)
            data = self.instr.query_str_list("TRACE:DATA?")
            if data:
                start = self.__center - self.__span
                stop = self.__center + self.__span
                freqs = list(map(lambda x: x, np.linspace(start, stop, len(data))))
                sl = dict(zip(freqs, data))
                if self.__record:
                    self.__slices_queue.append((datetime.now(), sl))
                    self.ui.lineEditStartTime.setText(
                        f"{self.__slices_queue[0][0].strftime("%H:%M:%S %d-%m-%Y")} ({(datetime.now()-self.__slices_queue[0][0]).total_seconds()} s)"
                    )
                    self.ui.lineEditSlices.setText(str(len(self.__slices_queue)))

                # spec = {}
                # spec["r"] = list(map(lambda x: x[0], self.__slices_queue))
                # spec["f"] = freqs
                # spec["m"] = list(map(lambda x: x[1], self.__slices_queue))
                # canvas_freq = MplSpecCanvas(spec, self.args["viewer"])
                # self.ui.verticalLayoutSpecInstr.addWidget(canvas_freq.add_toolbar())
                # self.ui.verticalLayoutSpecInstr.addWidget(canvas_freq)

                QApplication.processEvents()


def __enable_disable(self, enable):
    if enable:
        set_icon(self.ui.pushButtonConnect, icon_types.LINK_OFF)
    else:
        set_icon(self.ui.pushButtonConnect, icon_types.ADD_LINK)

    self.ui.pushButtonRecord.setEnabled(enable)
    self.ui.labelCenter.setEnabled(enable)
    self.ui.doubleSpinBoxCenter.setEnabled(enable)
    self.ui.labelSpan.setEnabled(enable)
    self.ui.doubleSpinBoxSpan.setEnabled(enable)
    self.ui.labelMin.setEnabled(enable)
    self.ui.doubleSpinBoxMin.setEnabled(enable)
    self.ui.labelMax.setEnabled(enable)
    self.ui.doubleSpinBoxMax.setEnabled(enable)
    self.ui.labelSweep.setEnabled(enable)
    self.ui.doubleSpinBoxSweep.setEnabled(enable)
    self.ui.labelOffsetsInstr.setEnabled(enable)
    self.ui.comboBoxOffsetsInstr.setEnabled(enable)
