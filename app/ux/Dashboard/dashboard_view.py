from Spectrogram import Spectrogram
from single_include import QFileDialog
from ux.MplSpecCanvas import MplSpecCanvas
from ux.Mpl2DPlotCanvas import Mpl2DPlotCanvas
from kernel.QtMger import set_icon, icon_types, remove_widgets


def init(self):
    set_icon(self.ui.pushButtonFileOpen, icon_types.FILE_OPEN)
    set_icon(self.ui.labelOffsetsView, icon_types.CADENCE, (30, 30))

    self.ui.comboBoxOffsetsView.currentIndexChanged.connect(
        lambda d: __comboBoxOffsetsViewCurrentIndexChanged(self, d)
    )

    bands = list(map(lambda x: f"{x["band"]}: {x["value"]}", self.args["lo"]))
    self.ui.comboBoxOffsetsView.addItems(bands)
    self.ui.pushButtonFileOpen.clicked.connect(lambda: __open_track(self))


def __comboBoxOffsetsViewCurrentIndexChanged(self, d):
    self.lo = self.args["lo"][d]["value"]
    __load_track(self)


def __open_track(self):
    filename, _ = QFileDialog.getOpenFileUrl(
        parent=None,
        caption="Open Spectrogram CSV",
        filter="CSV Files (*.csv);;All Files (*)",
    )

    self.filename = filename.path() if filename else self.filename
    __load_track(self)


def __load_track(self):
    def update_slice_canvas(data, plot, array, data_exact, span):

        # update time plot
        time = self.spec.time_slice(array[1])
        self.canvas_time = Mpl2DPlotCanvas(
            x=self.spec.spec["r"],
            y=time,
            xlim=span[0],
            labels=("time", "intensity"),
        )
        remove_widgets(self.ui.verticalLayoutTime)
        self.ui.verticalLayoutTime.addWidget(self.canvas_time.add_toolbar())
        self.ui.verticalLayoutTime.addWidget(self.canvas_time)

        # update freq plot
        freq = self.spec.freq_slice(array[0])
        self.canvas_freq = Mpl2DPlotCanvas(
            x=freq,
            y=self.spec.spec["f"],
            ylim=span[1],
            labels=("intensity", "frequency"),
        )
        remove_widgets(self.ui.verticalLayoutFreq)
        self.ui.verticalLayoutFreq.addWidget(self.canvas_freq.add_toolbar())
        self.ui.verticalLayoutFreq.addWidget(self.canvas_freq)

    if not self.filename:
        return

    remove_widgets(self.ui.verticalLayoutSpec)

    self.spec = Spectrogram()
    self.spec.read_file(self.filename, self.args["viewer"]["separator"], self.lo)
    self.canvas_freq = MplSpecCanvas(
        self.spec.spec,
        self.args["viewer"],
        lambda data, plot, array, data_exact, span: update_slice_canvas(
            data, plot, array, data_exact, span
        ),
    )
    self.ui.verticalLayoutSpec.addWidget(self.canvas_freq.add_toolbar())
    self.ui.verticalLayoutSpec.addWidget(self.canvas_freq)
