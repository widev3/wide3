import numpy as np
from matplotlib import colors
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)


class Mpl2DPlotCanvas(FigureCanvasQTAgg):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)
        self.__axes.set_xlabel("time")
        self.__axes.set_ylabel("freq")
        self.__im = self.__axes.plot(
            self.__x,
            self.__y,
            # norm=colors.PowerNorm(
            #     gamma=self.__conf["gamma"],
            #     vmin=np.min(self.__sp["m"]),
            #     vmax=np.max(self.__sp["m"]),
            # ),
            # cmap=self.__conf["cmap"],
            # aspect="auto",
            # interpolation="bilinear",
            # origin="lower",
            # extent=[
            #     self.__lo + min(self.__sp["r"]),
            #     self.__lo + max(self.__sp["r"]),
            #     self.__lo + min(self.__sp["f"]) / 1000000,
            #     self.__lo + max(self.__sp["f"]) / 1000000,
            # ],
        )

        self.__fig.colorbar(self.__im)
        super().__init__(self.__fig)

    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self)
        return self.toolbar
