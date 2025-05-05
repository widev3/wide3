from single_include import RsInstrument, traceback, datetime, QMessageBox, QTimer
from kernel.QtMger import MessageBox, WindowManager
from utils import start_prog, stop_prog
from kernel.comboBoxDialog.ComboBoxDialog import Ui_Dialog
from kernel.comboBoxDialog.UXComboBoxDialog import BHComboBoxDialog


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        stop_prog(self.ui.label, self.ui.progressBar)
        self.ui.pushButtonRefresh.clicked.connect(self.__search_instr)

    def __search_instr(self):
        key = None
        try:
            start_prog(self.ui.label, self.ui.progressBar, "Looking for instrument...")
            instr_list = RsInstrument.list_resources("?*")
            stop_prog(
                self.ui.label,
                self.ui.progressBar,
                "Nothing is happening in the background",
            )

            if instr_list:
                if not key and len(instr_list) == 1:
                    key = instr_list[0]
                elif key and key in instr_list:
                    print("autoconnection")
                else:
                    win = WindowManager(Ui_Dialog, BHComboBoxDialog, instr_list)
                    win.exec()
                    key = win.bh.text
            else:
                return MessageBox(
                    text="No instrument connected",
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
        if self.__instr and self.__instr.is_connection_active:
            self.__instr.close()
            self.__instr = None

    def __connect_instr(self, key):
        self.__disconnect_instr()

        try:
            self.__instr = RsInstrument(key, id_query=True, reset=True)
            idn = self.__instr_comm(cmd="*IDN?", case="query_str")

            now = datetime.datetime.now()
            self.__instr_comm("SYST:BEEP:KEY:VOL", 0)
            self.__instr_comm("SYST:BEEP:POV", "ON")
            self.__instr_comm("SYST:BEEP:VOL", 1)
            self.__instr_comm("SYST:DISP:UPD", "ON")
            self.__instr_comm("SYST:DATE", f"{now.year},{now.month},{now.day}")
            self.__instr_comm("SYST:TIME", f"{now.hour},{now.minute},{now.second}")
            self.__instr_comm("SYST:TZON", "01,00")
            self.__instr_comm("UNIT:LENG", "MET")
            self.__instr_comm("INST:SEL", "SAN")
            self.__instr_comm("UNIT:POW", "W")
            self.__instr_comm("INIT:CONT", "ON")

            self.__ax["connect_sa"].cla()
            self.__connect_sa_button = basic_view.Button(
                ax=self.__ax["connect_sa"], label="Disconnect SA"
            )
            self.__connect_sa_button.on_clicked(self.__disconnect_instr)

            self.__ax["record"].cla()
            self.__record_button = basic_view.Button(
                ax=self.__ax["record"], label="Start record"
            )
            self.__record_button.on_clicked(self.__start_record)

            self.__instr_update()

            basic_view.set_title(fig=self.__fig, subtitles=[key])
            basic_view.show_message(
                self.__conf["name"],
                f"""Device {key} is connected!
    IDN:\t{idn}
    Driver version:\t{self.__instr.driver_version}
    Visa manufacturer:\t{self.__instr.visa_manufacturer}
    Instrument full name:\t{self.__instr.full_instrument_model_name}
    Instrument options:\t{",".join(self.__instr.instrument_options)}""",
                icon=1,
            )
        except:
            return MessageBox(
                text=f"Error during connection device {key}:\n{traceback.format_exc()}",
                title="WOW",
                icon=QMessageBox.Icon.Critical,
                buttons=QMessageBox.StandardButton.Ok,
            ).result()
