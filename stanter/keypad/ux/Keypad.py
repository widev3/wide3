import globals
from single_include import Requester, QMessageBox
from despyner.QtMger import i_name, set_icon, get_icon_path, WindowManager

from despyner.MessageBox import MessageBox
from despyner.popupDialog.PopupDialog import Ui_Dialog as ui_popup_dialog
from despyner.popupDialog.UXPopupDialog import UXPopupDialog as ux_popup_dialog


class Keypad:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args

        self.ui.frameDirections.setEnabled(False)

        set_icon(self.ui.pushButtonN, i_name.ARROW_UPWARD, globals.theme, True)
        set_icon(self.ui.pushButtonS, i_name.ARROW_DOWNWARD, globals.theme, True)
        set_icon(self.ui.pushButtonE, i_name.ARROW_FORWARD, globals.theme, True)
        set_icon(self.ui.pushButtonW, i_name.ARROW_BACK, globals.theme, True)
        set_icon(self.ui.pushButtonStop, i_name.ADJUST, globals.theme, True)
        set_icon(self.ui.pushButtonAcquire, i_name.ADD_LINK, globals.theme, True)
        set_icon(self.ui.pushButtonRADEC, i_name.CHECK, globals.theme, True)
        set_icon(self.ui.pushButtonALTAZ, i_name.CHECK, globals.theme, True)

        self.ui.pushButtonAcquire.clicked.connect(self.pushButtonAcquire_click)

    def pushButtonAcquire_click(self):
        if not self.ui.lineEditEndpoint.text():
            WindowManager(
                ui_popup_dialog,
                ux_popup_dialog,
                {
                    "text": f"Insert a valid endpoint",
                    "image": get_icon_path(i_name.WARNING, globals.theme),
                },
                self.dialog,
            ).show()
            return

        self.requester = Requester(f"http://{self.ui.lineEditEndpoint.text()}:5000")
        sid = self.requester.get("/session/acquire")
        if sid:
            if "session_id" in sid:
                sid = sid["session_id"]
                self.ui.lineEditSID.setText(sid)

                self.ui.lineEditSID.setText(sid)
                self.ui.frameDirections.setEnabled(True)
                WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": f"session acquired!",
                        "image": get_icon_path(i_name.CHECK, globals.theme),
                    },
                    self.dialog,
                ).show()
            elif "message" in sid:
                WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": f"{sid["message"]}",
                        "image": get_icon_path(i_name.WARNING, globals.theme),
                    },
                    self.dialog,
                ).show()
            else:
                WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": "Unknown error",
                        "image": get_icon_path(i_name.ERROR, globals.theme),
                    },
                    self.dialog,
                ).show()
