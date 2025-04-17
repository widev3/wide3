import basic_view
import numpy as np
from scipy.signal import find_peaks


class Cursor:
    def __init__(self, ax, im):
        self.ax = ax
        self.im = im
        self.__x_ratio = len(self.im["spectrogram"]._A[0]) / (
            self.im["spectrogram"].get_extent()[1]
            - self.im["spectrogram"].get_extent()[0]
        )
        self.__y_ratio = len(self.im["spectrogram"]._A) / (
            self.im["spectrogram"].get_extent()[3]
            - self.im["spectrogram"].get_extent()[2]
        )
        self.__horizontal_line = ax["spectrogram"].axhline(
            color="black", linestyle="--", linewidth=1
        )
        self.__vertical_line = ax["spectrogram"].axvline(
            color="black", linestyle="--", linewidth=1
        )
        self.__fig = []
        self.__axvlines = {}
        self.__peaks_checkbuttons = []
        self.__options_radiobuttons = []

    def __position(self, event):
        (x, y) = (event.xdata, event.ydata)
        x_el = int((x - self.ax["spectrogram"].get_xlim()[0]) * self.__x_ratio)
        y_el = int((y - self.ax["spectrogram"].get_ylim()[0]) * self.__y_ratio)
        self.__vertical_line.set_xdata([x])
        self.__horizontal_line.set_ydata([y])
        return (x_el, y_el)

    def __zommed_limits(self):
        extent = self.im["spectrogram"].get_extent()
        xlim = self.ax["spectrogram"].get_xlim()
        ylim = self.ax["spectrogram"].get_ylim()
        el_xmin = int((xlim[0] - extent[0]) * self.__x_ratio)
        el_xmax = int((xlim[1] - extent[0]) * self.__x_ratio)
        el_ymin = int((ylim[0] - extent[2]) * self.__y_ratio)
        el_ymax = int((ylim[1] - extent[2]) * self.__y_ratio)

        return (
            self.im["spectrogram"]._A[el_ymin:el_ymax, el_xmin:el_xmax],
            el_xmin,
            el_xmax,
            el_ymin,
            el_ymax,
            xlim[0],
            xlim[1],
            ylim[0],
            ylim[1],
        )

    def __left_button_press_event_spectrogram(self, event):
        (x_el, y_el) = self.__position(event)
        zommed_limits, el_xmin, el_xmax, el_ymin, el_ymax, xmin, xmax, ymin, ymax = (
            self.__zommed_limits()
        )
        self.im["t_proj"].set_data(
            np.linspace(xmin, xmax, el_xmax - el_xmin), zommed_limits[y_el]
        )
        self.ax["t_proj"].relim()
        self.ax["t_proj"].autoscale()

        self.im["f_proj"].set_data(
            [x[x_el] for x in zommed_limits],
            np.linspace(ymin, ymax, el_ymax - el_ymin),
        )
        self.ax["f_proj"].relim()
        self.ax["f_proj"].autoscale()

    def __left_button_double_press_event(self, event, target):
        if target in self.im:
            mosaic = basic_view.generate_array(50, 50)

            # first column
            basic_view.fill_with_string(mosaic, (1, 2), (40, 50), target)

            # second column
            basic_view.fill_with_string(mosaic, (40, 2), (50, 10), "options", (1, 0))
            basic_view.fill_with_string(mosaic, (40, 10), (50, 50), "peaks", (1, 5))

            self.__fig, self.inner_ax = basic_view.create(
                self.ax[target].get_title(), mosaic, "icons/whistle_of_wind.png"
            )

            def on_options_radiobuttons_clicked(label):
                is_rotated = (
                    hasattr(self.ax[target], "is_rotated")
                    and self.ax[target].is_rotated
                )

                dim = 0
                data = {}
                if isinstance(self.im[target], basic_view.Line2D):
                    dim = 1
                    data = {
                        "x": self.im[target].get_data()[1 if is_rotated else 0],
                        "y": self.im[target].get_data()[0 if is_rotated else 1],
                    }
                elif isinstance(self.im[target], basic_view.AxesImage):
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
                elif label.startswith("FFT"):
                    if label == "FFT (frequency)":
                        frequency = 1
                        self.inner_ax[target].set_xlabel("Frequency [log10(Hz)]")
                    elif label == "FFT (time)":
                        frequency = -1
                        self.inner_ax[target].set_xlabel("Period [log10(sec)]")

                    self.inner_ax[target].set_ylabel(self.ax[target].get_ylabel())

                    if dim == 1:
                        yf = np.log10(np.abs(np.fft.rfft(data["y"], norm="forward")))
                        ff = (
                            np.fft.rfftfreq(
                                n=len(data["y"]), d=(data["x"][1] - data["x"][0]) / 1000
                            )
                            / 1000
                        )
                        ff = np.log10(list(map(lambda x: x**frequency, ff)))
                        data = {"x": ff, "y": yf}
                    elif dim == 2:
                        fft = np.log10(abs(np.fft.fft2(self.im[target]._A)))
                        data = {"X": fft}

                labels = []
                if dim == 1:
                    (peaks_index, peaks_height) = find_peaks(
                        data["y"], height=sum(data["y"]) / len(data["y"])
                    )
                    peaks_height = peaks_height["peak_heights"]
                    sorted_lists = sorted(
                        zip(peaks_index, peaks_height),
                        key=lambda x: x[1],
                        reverse=True,
                    )
                    (peaks_index, peaks_height) = zip(*sorted_lists)
                    peaks_index = list(peaks_index)[:20]
                    peaks_height = list(peaks_height)[:20]
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
                    vmax = np.max(data["X"])
                    vmin = np.min(data["X"])
                    self.inner_ax[target].imshow(
                        X=data["X"],
                        norm=basic_view.cm.colors.PowerNorm(
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
                            x=frequency, color="black", linestyle="--", linewidth=1
                        )

                self.inner_ax["peaks"].set_title(
                    f"""{self.inner_ax[target].get_xlabel()}
({self.inner_ax[target].get_ylabel()})"""
                )
                self.__peaks_checkbuttons = basic_view.CheckButtons(
                    ax=self.inner_ax["peaks"],
                    labels=labels,
                    actives=list(map(lambda x: False, labels)),
                    frame_props={"s": [64] * len(labels)},
                )
                self.__peaks_checkbuttons.on_clicked(
                    lambda x: (on_peaks_checkbuttons_clicked(x, data, dim))
                )
                self.inner_ax[target].set_title(
                    f"{self.ax[target].get_title()} ({label})"
                )
                basic_view.set_grid(self.inner_ax[target])

                self.__fig.canvas.draw()

            self.inner_ax["options"].set_title("Options")
            self.__options_radiobuttons = basic_view.RadioButtons(
                ax=self.inner_ax["options"],
                labels=["Data", "FFT (frequency)", "FFT (time)"],
                radio_props={"s": [64, 64, 64]},
            )
            self.__options_radiobuttons.on_clicked(on_options_radiobuttons_clicked)
            on_options_radiobuttons_clicked(
                self.__options_radiobuttons.labels[0].get_text()
            )

            basic_view.show()

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
        if event.button is basic_view.MouseButton.LEFT:
            if event.dblclick:
                self.__left_button_double_press_event(event, target)
            else:
                self.__left_button_press_event(event, target)
