import matplotlib
import matplotlib.pyplot as plt
import matplotlib.text
import numpy as np
from matplotlib import cm
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import CheckButtons, RadioButtons
from scipy.signal import find_peaks
from view.basic_view import basic_view


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
        self.__fig = []
        self.__axvlines = {}
        self.__peaks_checkbuttons = []
        self.__options_radiobuttons = []

    def __position(self, event):
        (x, y) = (event.xdata, event.ydata)
        x_el = int(x * self.__x_ratio)
        y_el = int(y * self.__y_ratio)
        self.__vertical_line.set_xdata([x])
        self.__horizontal_line.set_ydata([y])
        return (x_el, y_el)

    def __left_button_press_event_spectrogram(self, event):
        (x_el, y_el) = self.__position(event)
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
        if target in self.im:
            self.__fig = basic_view(self.ax[target].get_title())
            mosaic = [[target, "options"], [target, "peaks"]]
            self.inner_ax = self.__fig.subplot_mosaic(
                mosaic=mosaic,
                empty_sentinel=None,
                width_ratios=[5, 1],
                height_ratios=[1, 10],
            )

            def on_options_radiobuttons_clicked(label):
                is_rotated = (
                    hasattr(self.ax[target], "is_rotated")
                    and self.ax[target].is_rotated
                )

                dim = 0
                data = {}
                if isinstance(self.im[target], matplotlib.lines.Line2D):
                    dim = 1
                    data = {
                        "x": self.im[target].get_data()[1 if is_rotated else 0],
                        "y": self.im[target].get_data()[0 if is_rotated else 1],
                    }
                elif isinstance(self.im[target], matplotlib.image.AxesImage):
                    dim = 2
                    data = {"X": self.im[target]._A}

                self.inner_ax[target].clear()
                self.inner_ax["peaks"].clear()
                if label == "Data":
                    self.inner_ax[target].set_xlabel(self.ax[target].get_xlabel())
                    self.inner_ax[target].set_ylabel(self.ax[target].get_ylabel())
                    self.inner_ax[target].set_xlim(
                        self.ax[target].get_ylim()
                        if is_rotated
                        else self.ax[target].get_xlim()
                    )
                    self.inner_ax[target].set_ylim(
                        self.ax[target].get_xlim()
                        if is_rotated
                        else self.ax[target].get_ylim()
                    )
                elif label == "FFT":
                    self.inner_ax[target].set_xlabel("Frequency [Hz]")
                    self.inner_ax[target].set_ylabel(self.ax[target].get_ylabel())

                    if dim == 1:
                        yf = np.log10(np.abs(np.fft.rfft(data["y"], norm="forward")))
                        ff = np.log10(
                            np.fft.rfftfreq(
                                n=len(data["y"]), d=(data["x"][1] - data["x"][0]) / 1000
                            )
                            / 1000
                        )
                        data = {"x": ff, "y": yf}
                    elif dim == 2:
                        print("ciao")
                        fft = np.log10(abs(np.fft.fft2(self.im[target]._A)))
                        data = {"X": fft}

                labels = []
                if dim == 1:
                    (peaks_index, peaks_height) = find_peaks(data["y"], height=-5)
                    peaks_height = peaks_height["peak_heights"][:20]
                    sorted_lists = sorted(
                        zip(peaks_index, peaks_height),
                        key=lambda x: x[1],
                        reverse=True,
                    )
                    (peaks_index, peaks_height) = zip(*sorted_lists)
                    peaks_index = list(peaks_index)
                    peaks_height = list(peaks_height)
                    self.inner_ax[target].plot(
                        data["x"],
                        data["y"],
                        "-",
                        data["x"][peaks_index],
                        peaks_height,
                        "x",
                    )
                    labels = list(
                        map(
                            lambda x: f"{data['x'][x[1]]:.2e} ({peaks_height[x[0]]:.2e})",
                            enumerate(peaks_index),
                        )
                    )
                elif dim == 2:
                    vmax = max((max(sublist) for sublist in data["X"]))
                    vmin = min((min(sublist) for sublist in data["X"]))
                    self.inner_ax[target].imshow(
                        X=data["X"],
                        norm=cm.colors.PowerNorm(
                            gamma=self.im[target].norm.gamma, vmin=vmin, vmax=vmax
                        ),
                        cmap=self.im[target].get_cmap(),
                        aspect=self.im[target].axes.get_aspect(),
                        origin=self.im[target].origin,
                        extent=self.im[target].get_extent(),
                    )

                def on_peaks_checkbuttons_clicked(label, data, dim):
                    index = [
                        x.get_text() for x in self.__peaks_checkbuttons.labels
                    ].index(label)
                    frequency = 0
                    if dim == 1:
                        frequency = [data["x"][x] for x in peaks_index][index]
                    elif dim == 2:
                        frequency = 0

                    if label in self.__axvlines:
                        self.__axvlines[label].remove()
                        del self.__axvlines[label]
                    else:
                        self.__axvlines[label] = self.inner_ax[target].axvline(
                            x=frequency, color="r", linestyle="--"
                        )

                self.inner_ax["peaks"].set_title(
                    f"{self.inner_ax[target].get_xlabel()} ({self.inner_ax[target].get_ylabel()})"
                )
                self.__peaks_checkbuttons = CheckButtons(
                    ax=self.inner_ax["peaks"],
                    labels=labels,
                    actives=list(map(lambda x: False, labels)),
                    frame_props={"s": list(map(lambda x: 64, labels))},
                )
                self.__peaks_checkbuttons.on_clicked(
                    lambda x: (on_peaks_checkbuttons_clicked(x, data, dim))
                )
                self.inner_ax[target].set_title(
                    f"{self.ax[target].get_title()} ({label})"
                )
                self.inner_ax[target].grid(
                    True, linestyle="--", color="gray", alpha=0.7, which="both"
                )

                self.__fig.canvas.draw()

            self.inner_ax["options"].set_title("Options")
            self.__options_radiobuttons = RadioButtons(
                ax=self.inner_ax["options"],
                labels=["Data", "FFT"],
                radio_props={"s": [64, 64]},
            )
            self.__options_radiobuttons.on_clicked(on_options_radiobuttons_clicked)
            on_options_radiobuttons_clicked(
                self.__options_radiobuttons.labels[0].get_text()
            )

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
