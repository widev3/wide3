from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MplSpecCanvas(FigureCanvasQTAgg):
    def __init__(self, im):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.axes.imshow(im, interpolation="nearest", aspect="auto")
        super().__init__(self.fig)
