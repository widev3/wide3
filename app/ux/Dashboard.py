from ux.MplSpecCanvas import MplSpecCanvas
from single_include import (
    RsInstrument,
    traceback,
    datetime,
    QMessageBox,
    QFileDialog,
)
from utils import start_prog, stop_prog

from kernel.popupDialog.PopupDialog import Ui_Dialog as UIPopupDialog
from kernel.popupDialog.UXPopupDialog import UXPopupDialog

from kernel.comboBoxDialog.ComboBoxDialog import Ui_Dialog as UIComboBoxDialog
from kernel.comboBoxDialog.UXComboBoxDialog import UXComboBoxDialog

from kernel.QtMger import set_icon, icon_types, WindowManager, get_icon_path
from kernel.MessageBox import MessageBox

from spectrogram import reader

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        self.__instr = None
        stop_prog(self.ui.label, self.ui.progressBar)

        set_icon(self.ui.pushButtonConnect, icon_types.ADD_LINK)
        set_icon(self.ui.pushButtonFileOpen, icon_types.FILE_OPEN)
        set_icon(self.ui.pushButtonSettings, icon_types.SETTINGS)
        set_icon(self.ui.pushButtonInfo, icon_types.INFO)

        self.ui.pushButtonConnect.clicked.connect(self.__conn_disconn)
        self.ui.pushButtonFileOpen.clicked.connect(self.__open_track)
        self.ui.pushButtonSettings.clicked.connect(lambda x: None)
        self.ui.pushButtonInfo.clicked.connect(self.__info)

    def __conn_disconn(self):
        def __disconnect_instr(self):
            if self.__instr and self.__instr.is_connection_active:
                self.__instr.close()
                self.__instr = None

        def __connect_instr(self, key: str):
            if self.__instr:
                __disconnect_instr(self)

            try:
                self.__instr = RsInstrument(key, id_query=True, reset=True)

                now = datetime.now()
                self.__instr.write_str("SYST:BEEP:KEY:VOL 0")
                self.__instr.write_str("SYST:BEEP:POV ON")
                self.__instr.write_str("SYST:BEEP:VOL 1")
                self.__instr.write_str("SYST:DISP:UPD ON")
                self.__instr.write_str(f"SYST:DATE {now.year},{now.month},{now.day}")
                self.__instr.write_str(
                    f"SYST:TIME {now.hour},{now.minute},{now.second}"
                )
                self.__instr.write_str("SYST:TZON 01,00")
                self.__instr.write_str("UNIT:LENG MET")
                self.__instr.write_str("INST:SEL SAN")
                self.__instr.write_str("UNIT:POW W")
                self.__instr.write_str("INIT:CONT ON")

                args = {}
                args["text"] = f"Connected!"
                args["image"] = get_icon_path(icon_types.CHECK)
                WindowManager(UIPopupDialog, UXPopupDialog, args).show()

                return True
            except:
                MessageBox(
                    text=f"Error during connection device {key}:\n{traceback.format_exc()}",
                    title="WOW",
                    icon=QMessageBox.Icon.Critical,
                    buttons=QMessageBox.StandardButton.Ok,
                ).result()

                return False

        try:
            start_prog(self.ui.label, self.ui.progressBar, "Looking for instrument...")
            instr_list = RsInstrument.list_resources("?*")
            stop_prog(self.ui.label, self.ui.progressBar)

            if instr_list:
                key = None
                if "instr" in self.args and self.args["instr"] in instr_list:
                    key = self.args["instr"]
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

                if __connect_instr(self, key):
                    set_icon(self.ui.pushButtonConnect, icon_types.LINK_OFF)
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

    def __open_track(self):
        filename, _ = QFileDialog.getOpenFileUrl(
            parent=None,
            caption="Open Spectrogram CSV",
            filter="CSV Files (*.csv);;All Files (*)",
        )

        if filename:
            filename = filename.path()
            start_prog(self.ui.label, self.ui.progressBar, f"Reading {filename}...")

            pr, fr, sp = reader(filename, self.args["viewer"]["separator"])
            self.canvas = MplSpecCanvas(sp, self.args["viewer"])
            self.ui.gridLayout_4.addWidget(self.canvas.add_toolbar())
            self.ui.gridLayout_4.addWidget(self.canvas)
            self.canvas.fig.set_figheight(self.ui.frameSpec.height())
            self.canvas.fig.set_figwidth(self.ui.frameSpec.width())

            self.canvas_time = MplSpecCanvas(sp, self.args["viewer"])
            self.ui.gridLayout_5.addWidget(self.canvas_time.add_toolbar())
            self.ui.gridLayout_5.addWidget(self.canvas_time)
            self.canvas_time.fig.set_figheight(self.ui.frameTime.height())
            self.canvas_time.fig.set_figwidth(self.ui.frameTime.width())

            self.canvas_freq = MplSpecCanvas(sp, self.args["viewer"])
            self.ui.gridLayout_7.addWidget(self.canvas_freq.add_toolbar())
            self.ui.gridLayout_7.addWidget(self.canvas_freq)
            self.canvas_freq.fig.set_figheight(self.ui.frameFreq.height())
            self.canvas_freq.fig.set_figwidth(self.ui.frameFreq.width())

            stop_prog(self.ui.label, self.ui.progressBar)

    def __info(self):
        if self.__instr:
            idn = self.__instr.query_str("*IDN?")
            content = f"""IDN: {idn}
Driver version: {self.__instr.driver_version}
Visa manufacturer: {self.__instr.visa_manufacturer}
Instrument full name: {self.__instr.full_instrument_model_name}
Instrument options: {",".join(self.__instr.instrument_options)}"""
            MessageBox(
                text=content,
                title="Info",
                icon=QMessageBox.Icon.Information,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()
        else:
            args = {}
            args["text"] = f"Connect to get information about the instrument!"
            args["image"] = get_icon_path(icon_types.INFO)
            WindowManager(UIPopupDialog, UXPopupDialog, args).show()
