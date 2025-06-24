from Spectrogram import Spectrogram
from ux.MplSpecCanvas import MplSpecCanvas
from ux.Mpl2DPlotCanvas import Mpl2DPlotCanvas
from single_include import (
    RsInstrument,
    traceback,
    datetime,
    QMessageBox,
    QFileDialog,
    Qt,
)

from kernel.popupDialog.PopupDialog import Ui_Dialog as UIPopupDialog
from kernel.popupDialog.UXPopupDialog import UXPopupDialog

from kernel.comboBoxDialog.ComboBoxDialog import Ui_Dialog as UIComboBoxDialog
from kernel.comboBoxDialog.UXComboBoxDialog import UXComboBoxDialog

from kernel.QtMger import set_icon, icon_types, WindowManager, get_icon_path
from kernel.MessageBox import MessageBox


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        self.__instr = None
        self.__filename = None

        set_icon(self.ui.pushButtonConnect, icon_types.ADD_LINK)
        set_icon(self.ui.pushButtonFileOpen, icon_types.FILE_OPEN)
        set_icon(self.ui.pushButtonInfo, icon_types.INFO)
        set_icon(self.ui.labelCenter, icon_types.ADJUST, (30, 30))
        set_icon(self.ui.labelSpan, icon_types.ARROW_RANGE, (30, 30))
        set_icon(self.ui.labelMin, icon_types.ARROW_MENU_CLOSE, (30, 30))
        set_icon(self.ui.labelMax, icon_types.ARROW_MENU_OPEN, (30, 30))
        set_icon(self.ui.labelOffsets, icon_types.CADENCE, (30, 30))

        self.ui.comboBoxOffsets.currentIndexChanged.connect(
            self.__comboBoxOffsetsCurrentIndexChanged
        )

        self.ui.doubleSpinBoxCenter.valueChanged.connect(
            self.__doubleSpinBoxCenterValueChanged
        )

        self.ui.doubleSpinBoxSpan.valueChanged.connect(
            self.__doubleSpinBoxSpanValueChanged
        )

        self.ui.doubleSpinBoxMin.valueChanged.connect(
            self.__doubleSpinBoxMinValueChanged
        )

        self.ui.doubleSpinBoxMax.valueChanged.connect(
            self.__doubleSpinBoxMaxValueChanged
        )

        self.ui.comboBoxOffsets.addItems(
            list(map(lambda x: f"{x["band"]}: {x["value"]}", self.args["lo"]))
        )

        self.ui.pushButtonConnect.clicked.connect(self.__conn_disconn)
        self.ui.pushButtonFileOpen.clicked.connect(self.__open_track)
        self.ui.pushButtonInfo.clicked.connect(self.__info)

        self.dialog.setWindowState(Qt.WindowMaximized)

    def __comboBoxOffsetsCurrentIndexChanged(self, d):
        self.__lo = self.args["lo"][d]["value"]
        self.__load_track()

    def __doubleSpinBoxCenterValueChanged(self, d):
        self.ui.horizontalSliderCenter.setValue(d)

    def __doubleSpinBoxSpanValueChanged(self, d):
        self.ui.horizontalSliderSpan.setValue(d)

    def __doubleSpinBoxMinValueChanged(self, d):
        self.ui.horizontalSliderMin.setValue(d)

    def __doubleSpinBoxMaxValueChanged(self, d):
        self.ui.horizontalSliderMax.setValue(d)

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
            instr_list = RsInstrument.list_resources("?*")

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

        self.__filename = filename.path() if filename else self.__filename
        self.__load_track()

    def __load_track(self):

        def update_slice_canvas(data_coord, plot_coord, array_coord, exact_val_coord):
            self.canvas_time = Mpl2DPlotCanvas(time)
            self.ui.verticalLayoutTime.addWidget(self.canvas_time.add_toolbar())
            self.ui.verticalLayoutTime.addWidget(self.canvas_time)

            self.canvas_freq = Mpl2DPlotCanvas(freq)
            self.ui.verticalLayoutFreq.addWidget(self.canvas_freq.add_toolbar())
            self.ui.verticalLayoutFreq.addWidget(self.canvas_freq)

        if not self.__filename:
            return

        spec = Spectrogram()
        spec.read_file(self.__filename, self.args["viewer"]["separator"])
        self.canvas_freq = MplSpecCanvas(
            spec.spec,
            self.args["viewer"],
            self.__lo,
            lambda data_coord, plot_coord, array_coord, exact_val_coord: update_slice_canvas(
                data_coord, plot_coord, array_coord, exact_val_coord
            ),
        )
        self.ui.verticalLayoutSpec.addWidget(self.canvas_freq.add_toolbar())
        self.ui.verticalLayoutSpec.addWidget(self.canvas_freq)

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
