import globals
import os.path
from single_include import Requester, QObject, Signal, time, QThread, Slot, json
from despyner.QtMger import i_name, set_icon, get_icon_path, WindowManager

from despyner.popupDialog.PopupDialog import Ui_Dialog as ui_popup_dialog
from despyner.popupDialog.UXPopupDialog import UXPopupDialog as ux_popup_dialog

last_session = "last.json"


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
                if j and j[0] == 200:
                    self.__par.worker.progress.emit(j[1])

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
        self.__last = None
        self.__coord = None
        self.__range = None
        self.__behavior = None
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

        self.ui.comboBoxCoords.currentTextChanged.connect(
            lambda x: self.comboBoxCoords_currentTextChanged(x, False)
        )
        self.ui.comboBoxCoords.setCurrentIndex(1)
        self.ui.comboBoxCoords.setCurrentIndex(0)
        self.ui.comboBoxCoords.currentTextChanged.disconnect()
        self.ui.comboBoxCoords.currentTextChanged.connect(
            self.comboBoxCoords_currentTextChanged
        )

        self.ui.comboBoxRanges.currentTextChanged.connect(
            lambda x: self.comboBoxRanges_currentTextChanged(x, False)
        )
        self.ui.comboBoxRanges.setCurrentIndex(1)
        self.ui.comboBoxRanges.setCurrentIndex(0)
        self.ui.comboBoxRanges.currentTextChanged.disconnect()
        self.ui.comboBoxRanges.currentTextChanged.connect(
            self.comboBoxRanges_currentTextChanged
        )

        self.ui.comboBoxBehavior.currentTextChanged.connect(
            lambda x: self.comboBoxBehavior_currentTextChanged(x, False)
        )
        self.ui.comboBoxBehavior.setCurrentIndex(1)
        self.ui.comboBoxBehavior.setCurrentIndex(0)
        self.ui.comboBoxBehavior.currentTextChanged.disconnect()
        self.ui.comboBoxBehavior.currentTextChanged.connect(
            self.comboBoxBehavior_currentTextChanged
        )

        if os.path.isfile(last_session):
            with open(last_session) as f:
                self.__last = json.load(f)
                if "server_endpoint" in self.__last and "sid" in self.__last:
                    self.requester = Requester(
                        f"http://{self.__last["server_endpoint"]}:5000",
                        headers={"Authorization": self.__last["sid"]},
                    )
                    self.ui.lineEditEndpoint.setText(self.__last["server_endpoint"])
                    self.__release()
                    self.__acquire()

                if "coords" in self.__last:
                    self.ui.comboBoxCoords.setCurrentText(self.__last["coords"])

                if "range" in self.__last:
                    self.ui.comboBoxRanges.setCurrentText(self.__last["range"])

                if "behavior" in self.__last:
                    self.ui.comboBoxBehavior.setCurrentText(self.__last["behavior"])

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

    def __upsert_last(self, key, value):
        if os.path.isfile(last_session):
            with open(last_session, "r") as file:
                last = json.load(file)
            last[key] = value
            with open(last_session, "w") as file:
                json.dump(last, file, indent=4)

    def __release(self):
        self.__sid = None
        sid = self.requester.get("/session/release")
        if sid:
            if ("message" in sid[1] and sid[1]["message"] == "OK") or (
                "error" in sid[1] and sid[1]["error"] == "no active session"
            ):
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
            elif "error" in sid[1]:
                return WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": f"{sid[1]["error"]}",
                        "image": get_icon_path(i_name.ERROR, globals.theme),
                    },
                    self.dialog,
                ).show()

    def __acquire(self):
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
            if "session_id" in sid[1]:
                sid = sid[1]["session_id"]
                self.__sid = sid
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
            elif "message" in sid[1]:
                return WindowManager(
                    ui_popup_dialog,
                    ux_popup_dialog,
                    {
                        "text": f"{sid[1]["message"]}",
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

    def pushButtonLink_clicked(self):
        if self.__sid:
            self.__release()
        else:
            self.__acquire()

    def pushButtonNSEW_clicked(self, x):
        if x == "N":
            print(x)

    def comboBoxCoords_currentTextChanged(self, text: str, save: bool = True):
        self.__coord = text
        coords = self.__coord.split("/")
        self.ui.label1Coord1.setText(coords[0])
        self.ui.label1Coord2.setText(coords[1])
        self.ui.label2Coord1.setText(coords[0])
        self.ui.label2Coord2.setText(coords[1])
        if save:
            self.__upsert_last("coords", self.__coord)

    def comboBoxRanges_currentTextChanged(self, text: str, save: bool = True):
        self.__range = text
        if save:
            self.__upsert_last("range", self.__range)

    def comboBoxBehavior_currentTextChanged(self, text: str, save: bool = True):
        self.__behavior = text
        self.ui.frameOffset.setEnabled(self.__behavior != "Follow")
        if save:
            self.__upsert_last("behavior", self.__behavior)
