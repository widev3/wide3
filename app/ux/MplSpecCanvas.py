import numpy as np
from matplotlib import colors
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)


class MplSpecCanvas(FigureCanvasQTAgg):
    def __init__(self, sp, conf, lo, button_press_event=None):
        self.sp = sp
        self.__conf = conf
        self.__lo = lo
        self.__button_press_event = button_press_event

        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)
        self.__axes.set_xlabel("time")
        self.__axes.set_ylabel("freq")
        self.__im = self.__axes.imshow(
            X=self.sp["m"],
            norm=colors.PowerNorm(
                gamma=self.__conf["gamma"],
                vmin=np.min(self.sp["m"]),
                vmax=np.max(self.sp["m"]),
            ),
            cmap=self.__conf["cmap"],
            aspect="auto",
            interpolation="bilinear",
            origin="lower",
            extent=[
                self.__lo + min(self.sp["r"]),
                self.__lo + max(self.sp["r"]),
                self.__lo + min(self.sp["f"]) / 1000000,
                self.__lo + max(self.sp["f"]) / 1000000,
            ],
        )

        self.__fig.canvas.mpl_connect(
            "button_press_event", self.__internal_button_press_event
        )

        self.__fig.colorbar(self.__im)
        super().__init__(self.__fig)

    def __internal_button_press_event(self, x):
        if self.__button_press_event:
            index_x = list(filter(lambda y: x.xdata >= y[1], enumerate(self.sp["r"])))[
                -1
            ]
            index_y = list(filter(lambda y: x.ydata >= y[1], enumerate(self.sp["f"])))[
                -1
            ]
            data_coord = (x.xdata, x.ydata)
            plot_coord = (x.x, x.y)
            array_coord = (index_x[0], index_y[0])
            exact_val_coord = (index_x[1], index_y[1])
            self.__button_press_event(
                data_coord, plot_coord, array_coord, exact_val_coord
            )

    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self)
        return self.toolbar
