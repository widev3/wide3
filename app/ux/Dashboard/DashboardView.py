import globals
from Spectrogram import Spectrogram
from single_include import QFileDialog
from ux.MplSpecCanvas import MplSpecCanvas
from ux.Mpl2DPlotCanvas import Mpl2DPlotCanvas
from despyner.QtMger import set_icon, icon_name


class DashboardView:
    def __init__(self, parent):
        self.__parent = parent
        self.__canvas_spec = None
        self.__filename = None

        set_icon(
            self.__parent.ui.pushButtonFileOpen,
            icon_name.FILE_OPEN,
            globals.theme,
            True,
        )
        set_icon(
            self.__parent.ui.labelOffsetsView,
            icon_name.CADENCE,
            globals.theme,
            True,
            (30, 30),
        )

        self.__parent.ui.comboBoxOffsetsView.currentIndexChanged.connect(
            self.__comboBoxOffsetsViewCurrentIndexChanged
        )

        self.__parent.ui.horizontalSliderGammaView.valueChanged.connect(
            self.__horizontalSliderGammaViewValueChanged
        )

        self.__parent.ui.horizontalSliderGammaView.setValue(
            self.__parent.args["viewer"]["gamma"] * 1000
        )

        self.__parent.ui.comboBoxOffsetsView.addItems(self.__parent.bands)
        self.__parent.ui.pushButtonFileOpen.clicked.connect(self.__open_track)

        self.__canvas_spec = MplSpecCanvas(
            lambda a, b, c, d, e: self.update_slice_canvas(a, b, c, d, e)
        )
        self.__parent.ui.verticalLayoutSpec.addWidget(self.__canvas_spec.get_toolbar())
        self.__parent.ui.verticalLayoutSpec.addWidget(self.__canvas_spec)

        self.__canvas_time = Mpl2DPlotCanvas(labels=("time", "intensity"))
        self.__parent.ui.verticalLayoutTime.addWidget(self.__canvas_time.get_toolbar())
        self.__parent.ui.verticalLayoutTime.addWidget(self.__canvas_time)

        self.__canvas_freq = Mpl2DPlotCanvas(labels=("intensity", "frequency"))
        self.__parent.ui.verticalLayoutFreq.addWidget(self.__canvas_freq.get_toolbar())
        self.__parent.ui.verticalLayoutFreq.addWidget(self.__canvas_freq)

    def __comboBoxOffsetsViewCurrentIndexChanged(self, d):
        self.__lo = self.__parent.args["lo"][d]["value"]
        self.__load_track()

    def __horizontalSliderGammaViewValueChanged(self, d):
        d /= 1000
        self.__parent.ui.labelGammaView.setText(str(d))
        if self.__canvas_spec:
            self.__canvas_spec.__im.norm.gamma = d
            self.__canvas_spec.__fig.canvas.draw()
            self.__canvas_spec.__fig.canvas.flush_events()

    def __open_track(self):
        filename, _ = QFileDialog.getOpenFileUrl(
            parent=None,
            caption="Open Spectrogram CSV",
            filter="CSV Files (*.csv);;All Files (*)",
        )

        self.__filename = filename.path() if filename else self.__filename
        self.__load_track()

    def update_slice_canvas(self, data, plot, array, data_exact, span):
        # update time plot
        time = self.__spec.time_slice(array[1])
        xy = zip(self.__spec.spec["r"], time)
        xy = list(filter(lambda x: x[0] >= span[0][0] and x[0] <= span[0][1], xy))
        self.__canvas_time.set_data(
            list(map(lambda x: x[0], xy)), list(map(lambda x: x[1], xy))
        )

        # update freq plot
        freq = self.__spec.freq_slice(array[0])
        xy = zip(freq, self.__spec.spec["f"])
        xy = list(filter(lambda x: x[1] >= span[1][0] and x[1] <= span[1][1], xy))
        self.__canvas_freq.set_data(
            list(map(lambda x: x[0], xy)), list(map(lambda x: x[1], xy))
        )

    def __load_track(self):
        if not self.__filename:
            return

        self.__spec = Spectrogram()
        self.__spec.read_file(
            self.__filename, self.__parent.args["viewer"]["separator"], self.__lo
        )
        self.__canvas_spec.set_data(self.__spec.spec, self.__parent.args["viewer"])
