from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)


class Mpl2DPlotCanvas(FigureCanvasQTAgg):
    def __init__(self, x, y, xlim=None, ylim=None, labels: str | str = None):
        self.__x = x
        self.__y = y

        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)

        if labels:
            self.__axes.set_xlabel(labels[0])
            self.__axes.set_ylabel(labels[1])

        self.__im = self.__axes.plot(self.__x, self.__y)

        if xlim:
            self.__axes.set_xlim(xlim)

        if ylim:
            self.__axes.set_ylim(ylim)

        super().__init__(self.__fig)

    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self)
        return self.toolbar
