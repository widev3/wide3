import numpy as np
from matplotlib import colors
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar,
)


class MplSpecCanvas(FigureCanvasQTAgg):
    def __init__(self, sp, conf, button_press_event=None):
        self.sp = sp
        self.__conf = conf
        self.__button_press_event = button_press_event

        self.__fig = Figure()
        self.__axes = self.__fig.add_subplot(111)
        self.__axes.set_xlabel("time")
        self.__axes.set_ylabel("frequency")
        self.im = self.__axes.imshow(
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
                min(self.sp["r"]),
                max(self.sp["r"]),
                min(self.sp["f"]),
                max(self.sp["f"]),
            ],
        )

        self.__xlim = self.im.get_extent()[2:4]
        self.__ylim = self.im.get_extent()[0:2]

        self.__fig.canvas.mpl_connect(
            "button_press_event", self.__internal_button_press_event
        )
        self.__axes.callbacks.connect("xlim_changed", self.__internal_xlim_changed)
        self.__axes.callbacks.connect("ylim_changed", self.__internal_ylim_changed)

        self.__fig.colorbar(self.im)
        super().__init__(self.__fig)

    def __internal_button_press_event(self, x):
        if self.__button_press_event:
            idx_x = list(filter(lambda y: x.xdata >= y[1], enumerate(self.sp["r"])))[-1]
            idx_y = list(filter(lambda y: x.ydata >= y[1], enumerate(self.sp["f"])))[-1]

            data = (x.xdata, x.ydata)  # respect of plot data (interpol)
            plot = (x.x, x.y)  # respect of plot frame
            array = (idx_x[0], idx_y[0])  # respect of array indices
            data_exact = (idx_x[1], idx_y[1])  # respect of plot data (no interpol)

            span = (self.__xlim, self.__ylim)  # respect of plot data (interpol)
            # TODO complete with X and Y components of span
            idx_x = list(filter(lambda y: span[0] >= y[1], enumerate(self.sp["r"])))[-1]
            idx_y = list(filter(lambda y: span[1] >= y[1], enumerate(self.sp["f"])))[-1]
            span_array = (idx_x[0], idx_y[0])  # span respect of array indices
            span_exact = (idx_x[1], idx_y[1])  # span respect of plot data (no interpol)

            self.__button_press_event(
                data, plot, array, data_exact, span, span_array, span_exact
            )

    def __internal_xlim_changed(self, x):
        self.__xlim = x

    def __internal_ylim_changed(self, y):
        self.__ylim = y

    def add_toolbar(self):
        self.toolbar = NavigationToolbar(self)
        return self.toolbar
