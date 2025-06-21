import numpy as np
from matplotlib import colors
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MplSpecCanvas(FigureCanvasQTAgg):
    def __init__(self, sp, v_conf):
        lo = 0
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        # self.axes.imshow(im, interpolation="nearest", aspect="auto")
        self.axes.imshow(
            X=sp["m"],
            norm=colors.PowerNorm(
                gamma=v_conf["gamma"], vmin=np.min(sp["m"]), vmax=np.max(sp["m"])
            ),
            cmap=v_conf["cmap"],
            aspect="auto",
            origin="lower",
            extent=[
                lo + min(sp["r"]),
                lo + max(sp["r"]),
                lo + min(sp["f"]) / 1000000,
                lo + max(sp["f"]) / 1000000,
            ],
        )
        super().__init__(self.fig)
