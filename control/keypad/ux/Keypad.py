import globals
import os.path
from single_include import Requester, QObject, Signal, time, QThread, Slot, json
from despyner.QtMger import i_name, set_icon, get_icon_path, WindowManager

from despyner.popupDialog.PopupDialog import Ui_Dialog as ui_popup_dialog
from despyner.popupDialog.UXPopupDialog import UXPopupDialog as ux_popup_dialog


class Worker(QObject):
    progress = Signal(tuple)

    def set_parent(self, par):
        self.__par = par

    def run(self):
        self.__run = False
        while True:
            time.sleep(2)
            while self.__run:
                time.sleep(2)
                j = self.__par.requester.get("/mount/status")
                self.__par.worker.progress.emit(j)

    def stop(self):
        self.__run = False

    def start(self):
        self.__run = True


class Keypad:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args

        self.__sid = None
        self.__coord = None
        self.__range = None
        self.__status = {}

        self.worker = Worker()
        self.worker.set_parent(self)
        self.worker.progress.connect(lambda j: self.__update_status(j))

        self.__thread = QThread()
        self.__thread.started.connect(self.worker.run)
        self.worker.moveToThread(self.__thread)
        self.__thread.start()

        self.ui.frameDirections.setEnabled(False)

        set_icon(self.ui.pushButtonN, i_name.ARROW_UPWARD, globals.theme)
        set_icon(self.ui.pushButtonS, i_name.ARROW_DOWNWARD, globals.theme)
        set_icon(self.ui.pushButtonE, i_name.ARROW_FORWARD, globals.theme)
        set_icon(self.ui.pushButtonW, i_name.ARROW_BACK, globals.theme)
        set_icon(self.ui.pushButtonStop, i_name.ADJUST, globals.theme)
        set_icon(self.ui.pushButtonLink, i_name.ADD_LINK, globals.theme)
        set_icon(self.ui.pushButtonRADEC, i_name.CHECK, globals.theme)

        self.ui.pushButtonLink.clicked.connect(self.pushButtonLink_clicked)
        self.ui.pushButtonN.clicked.connect(lambda: self.pushButtonNSEW_clicked("N"))
        self.ui.pushButtonS.clicked.connect(lambda: self.pushButtonNSEW_clicked("S"))
        self.ui.pushButtonE.clicked.connect(lambda: self.pushButtonNSEW_clicked("E"))
        self.ui.pushButtonW.clicked.connect(lambda: self.pushButtonNSEW_clicked("W"))
        self.ui.pushButtonStop.clicked.connect(lambda: self.pushButtonNSEW_clicked("O"))

        self.ui.comboBoxRanges.currentTextChanged.connect(
            self.comboBoxRanges_currentTextChanged
        )
        self.ui.comboBoxRanges.setCurrentIndex(1)
        self.ui.comboBoxRanges.setCurrentIndex(0)

        self.ui.comboBoxCoords.currentIndexChanged.connect(
            self.comboBoxCoords_currentIndexChanged
        )
        self.ui.comboBoxCoords.setCurrentIndex(1)
        self.ui.comboBoxCoords.setCurrentIndex(0)

    @Slot(tuple)
    def __update_status(self, j):
        if "location" in j:
            v = j["location"]
            self.__status["location"] = v
            self.ui.lineEditLocation.setText(str(v))

        if "offset" in j:
            v = j["offset"]
            self.__status["offset"] = v
            self.ui.lineEditOffset.setText(str(v))

        if "position" in j:
            v = j["position"]
            self.__status["position"] = v
            self.ui.lineEditPosition.setText(str(v))

        if "target" in j:
            v = j["target"]
            self.__status["target"] = v
            self.ui.lineEditTarget.setText(str(v))

        if "bh" in j:
            v = j["bh"]
            self.__status["bh"] = v
            self.ui.lineEditBehavior.setText(str(v))

        if "is_running" in j:
            v = j["is_running"]
            self.__status["is_running"] = v
            self.ui.lineEditIsRunning.setText(str(v))

    def pushButtonLink_clicked(self):
        if self.__sid:
            sid = self.requester.get("/session/release")
            if "message" in sid:
                if sid["message"] == "OK":
                    self.ui.lineEditSID.setText("")
                    self.ui.frameDirections.setEnabled(False)
                    set_icon(self.ui.pushButtonLink, i_name.ADD_LINK, globals.theme)
                    self.worker.stop()
                    self.requester = Requester(
                        f"http://{self.ui.lineEditEndpoint.text()}:5000"
                    )

                    return WindowManager(
                        ui_popup_dialog,
                        ux_popup_dialog,
                        {
                            "text": f"Session released",
                            "image": get_icon_path(i_name.CHECK, globals.theme),
                        },
                        self.dialog,
                    ).show()

                return WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": f"{sid["message"]}",
                        "image": get_icon_path(i_name.ERROR, globals.theme),
                    },
                    self.dialog,
                ).show()
        else:
            last_session = "last.json"
            if os.path.isfile(last_session):
                with open(last_session) as f:
                    j = json.load(f)
                    self.ui.lineEditEndpoint.setText(j["server_endpoint"])
                    self.requester = Requester(
                        f"http://{j["server_endpoint"]}:5000",
                        headers={"Authorization": j["sid"]},
                    )
                    sid = self.requester.get("/session/release")

            endpoint = self.ui.lineEditEndpoint.text()
            if not endpoint:
                return WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": f"Insert an endpoint",
                        "image": get_icon_path(i_name.WARNING, globals.theme),
                    },
                    self.dialog,
                ).show()

            self.requester = Requester(f"http://{endpoint}:5000")
            sid = self.requester.get("/session/acquire")
            if sid:
                if "session_id" in sid:
                    sid = sid["session_id"]
                    self.__sid = sid
                    self.ui.lineEditSID.setText(self.__sid)

                    self.ui.lineEditSID.setText(self.__sid)
                    self.ui.frameDirections.setEnabled(True)
                    set_icon(self.ui.pushButtonLink, i_name.LINK_OFF, globals.theme)

                    self.requester = Requester(
                        f"http://{endpoint}:5000", headers={"Authorization": self.__sid}
                    )
                    self.worker.start()

                    with open(last_session, "w", encoding="utf-8") as f:
                        json.dump(
                            {
                                "server_endpoint": f"{endpoint}",
                                "sid": f"{self.__sid}",
                            },
                            f,
                            indent=4,
                        )

                    return WindowManager(
                        ui_popup_dialog,
                        ux_popup_dialog,
                        {
                            "text": f"Session acquired",
                            "image": get_icon_path(i_name.CHECK, globals.theme),
                        },
                        self.dialog,
                    ).show()

                if "message" in sid:
                    return WindowManager(
                        ui_popup_dialog,
                        ux_popup_dialog,
                        {
                            "text": f"{sid["message"]}",
                            "image": get_icon_path(i_name.WARNING, globals.theme),
                        },
                        self.dialog,
                    ).show()

            return WindowManager(
                ui_popup_dialog,
                ux_popup_dialog,
                {
                    "text": "Unknown error",
                    "image": get_icon_path(i_name.ERROR, globals.theme),
                },
                self.dialog,
            ).show()

    def pushButtonNSEW_clicked(self, x):
        if x == "N":
            print(x)

    def comboBoxCoords_currentIndexChanged(self, index: int):
        self.__coord = [
            self.ui.comboBoxCoords.itemText(i)
            for i in range(self.ui.comboBoxCoords.count())
        ][index]
        coords = self.__coord.split("/")
        self.ui.labelCoord1.setText(coords[0])
        self.ui.labelCoord2.setText(coords[1])

    def comboBoxRanges_currentTextChanged(self, text: str):
        self.__range = text
