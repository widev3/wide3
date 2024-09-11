import matplotlib.image
import numpy as np
import matplotlib
from matplotlib.backend_bases import MouseButton
from view.basic_view import basic_view, plt
from matplotlib import cm


class Cursor:
    def __init__(self, ax, im, spectrogram):
        self.ax = ax
        self.im = im
        self.__spectrogram = spectrogram
        self.__x_ratio = len(self.im["spectrogram"]._A[0]) / (
            self.im["spectrogram"].get_extent()[1]
            - self.im["spectrogram"].get_extent()[0]
        )
        self.__y_ratio = len(self.im["spectrogram"]._A) / (
            self.im["spectrogram"].get_extent()[3]
            - self.im["spectrogram"].get_extent()[2]
        )
        self.__horizontal_line = ax["spectrogram"].axhline(color="k", ls="--", lw=0.5)
        self.__vertical_line = ax["spectrogram"].axvline(color="k", ls="--", lw=0.5)

    def __position(self, event):
        x, y = event.xdata, event.ydata
        x_el = int(x * self.__x_ratio)
        y_el = int(y * self.__y_ratio)
        self.__vertical_line.set_xdata([x])
        self.__horizontal_line.set_ydata([y])
        return x_el, y_el

    def __left_button_press_event_spectrogram(self, event):
        x_el, y_el = self.__position(event)
        self.im["t_proj"].set_data(
            np.linspace(
                min(self.__spectrogram["t"]),
                max(self.__spectrogram["t"]),
                num=len(self.__spectrogram["i"][0]),
            ),
            self.im["spectrogram"]._A[y_el],
        )
        lim = self.ax["t_proj"].get_xlim()
        self.ax["t_proj"].relim()
        self.ax["t_proj"].autoscale()
        self.ax["t_proj"].set_xlim(lim)

        self.im["f_proj"].set_data(
            [x[x_el] for x in self.im["spectrogram"]._A],
            np.linspace(
                min(self.__spectrogram["f"] / 1000000),
                max(self.__spectrogram["f"] / 1000000),
                num=len(self.__spectrogram["i"]),
            ),
        )
        lim = self.ax["f_proj"].get_ylim()
        self.ax["f_proj"].relim()
        self.ax["f_proj"].autoscale()
        self.ax["f_proj"].set_ylim(lim)

    def __left_button_double_press_event(self, event, target):
        fig = basic_view(self.ax[target].get_title())
        mosaic = [[target]]
        ax = fig.subplot_mosaic(mosaic=mosaic, empty_sentinel=None)
        is_rotated = (
            hasattr(self.ax[target], "is_rotated") and self.ax[target].is_rotated
        )
        if isinstance(self.im[target], matplotlib.lines.Line2D):
            ax[target].plot(
                self.im[target].get_data()[(1 if is_rotated else 0)],
                self.im[target].get_data()[(0 if is_rotated else 1)],
            )
        elif isinstance(self.im[target], matplotlib.image.AxesImage):
            ax[target].imshow(
                X=self.im[target]._A,
                norm=self.im[target].norm,
                cmap=self.im[target].get_cmap(),
                aspect=self.im[target].axes.get_aspect(),
                origin=self.im[target].origin,
                extent=self.im[target].get_extent(),
            )

        ax[target].set_title(self.ax[target].get_title())
        ax[target].set_xlabel(self.ax[target].get_xlabel())
        ax[target].set_ylabel(self.ax[target].get_ylabel())
        ax[target].set_xlim(self.ax[target].get_ylim() if is_rotated else self.ax[target].get_xlim())
        ax[target].set_ylim(self.ax[target].get_xlim() if is_rotated else self.ax[target].get_ylim())
        ax[target].grid(True, linestyle="--", color="gray", alpha=0.7)

        plt.show()

    def __left_button_press_event(self, event, target):
        if target == "spectrogram":
            self.__left_button_press_event_spectrogram(event=event)

    def __target(self, event):
        if event.inaxes:
            ax = event.inaxes
            for label, ax2 in self.ax.items():
                if ax == ax2:
                    return label

    def button_press_event(self, event):
        target = self.__target(event=event)
        if event.button is MouseButton.LEFT:
            if event.dblclick:
                self.__left_button_double_press_event(event, target)
            else:
                self.__left_button_press_event(event, target)
