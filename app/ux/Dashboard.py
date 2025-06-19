from threading import Timer
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

from kernel.QtMger import set_icon, icon_types, WindowManager, MessageBox, get_icon_path


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        self.instr = None
        stop_prog(self.ui.label, self.ui.progressBar)

        set_icon(self.ui.pushButtonRefresh, icon_types.REFRESH)
        set_icon(self.ui.pushButtonFileOpen, icon_types.FILE_OPEN)
        set_icon(self.ui.pushButtonSettings, icon_types.SETTINGS)

        self.ui.pushButtonRefresh.clicked.connect(self.__search_instr)
        self.ui.pushButtonFileOpen.clicked.connect(self.__open_track)

    def __search_instr(self):
        key = None
        try:
            start_prog(self.ui.label, self.ui.progressBar, "Looking for instrument...")
            instr_list = RsInstrument.list_resources("?*")
            stop_prog(self.ui.label, self.ui.progressBar)

            if instr_list:
                if len(instr_list) == 1:
                    key = instr_list[0]
                    res = MessageBox(
                        text=f"Connect to {key}? It is the only instrument available.",
                        title="WOW",
                        icon=QMessageBox.Icon.Question,
                        buttons=QMessageBox.StandardButton.Yes
                        | QMessageBox.StandardButton.No,
                    ).result()
                    if res == QMessageBox.StandardButton.No:
                        key = None
                elif key and key in instr_list:
                    print("autoconnection")
                else:
                    win = WindowManager(UIComboBoxDialog, UXComboBoxDialog, instr_list)
                    win.exec()
                    key = win.bh.text
            else:
                return MessageBox(
                    text="No instrument available",
                    title="WOW",
                    icon=QMessageBox.Icon.Warning,
                    buttons=QMessageBox.StandardButton.Ok,
                ).result()
        except:
            return MessageBox(
                text=f"Error during searching devices:\n{traceback.format_exc()}",
                title="WOW",
                icon=QMessageBox.Icon.Critical,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()

        self.__connect_instr(key)

    def __disconnect_instr(self):
        if self.instr and self.instr.is_connection_active:
            self.instr.close()
            self.instr = None

    def __connect_instr(self, key: str | None):
        if not key:
            return

        if self.instr:
            self.__disconnect_instr()

        try:
            self.instr = RsInstrument(key, id_query=True, reset=True)
            idn = self.instr.query_str("*IDN?")

            now = datetime.now()
            self.instr.write_str("SYST:BEEP:KEY:VOL 0")
            self.instr.write_str("SYST:BEEP:POV ON")
            self.instr.write_str("SYST:BEEP:VOL 1")
            self.instr.write_str("SYST:DISP:UPD ON")
            self.instr.write_str(f"SYST:DATE {now.year},{now.month},{now.day}")
            self.instr.write_str(f"SYST:TIME {now.hour},{now.minute},{now.second}")
            self.instr.write_str("SYST:TZON 01,00")
            self.instr.write_str("UNIT:LENG MET")
            self.instr.write_str("INST:SEL SAN")
            self.instr.write_str("UNIT:POW W")
            self.instr.write_str("INIT:CONT ON")

            args = {}
            args["text"] = f"Connected!"
            # args["icon"] = QtWidgets.QStyle.StandardPixmap.SP_DialogOkButton
            args["image"] = get_icon_path(icon_types.CHECK)
            # IDN:\t{idn}
            # Driver version:\t{self.instr.driver_version}
            # Visa manufacturer:\t{self.instr.visa_manufacturer}
            # Instrument full name:\t{self.instr.full_instrument_model_name}
            # Instrument options:\t{",".join(self.instr.instrument_options)}"""
            return WindowManager(UIPopupDialog, UXPopupDialog, args).show()
        except:
            return MessageBox(
                text=f"Error during connection device {key}:\n{traceback.format_exc()}",
                title="WOW",
                icon=QMessageBox.Icon.Critical,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()

    def __open_track(self):
        filename, _ = QFileDialog.getOpenFileUrl(
            parent=None,
            caption="Save CSV",
            filter="CSV Files (*.csv);;All Files (*)",
        )
        if filename:
            start_prog(self.ui.label, self.ui.progressBar, f"Reading {filename}...")
            instr_list = RsInstrument.list_resources("?*")
            stop_prog(self.ui.label, self.ui.progressBar)
