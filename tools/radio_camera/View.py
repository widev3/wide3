import os
import numpy as np
from radio_camera.Lims import Lims
from matplotlib.ticker import AutoMinorLocator
from Config import Config
from radio_camera.Cursor import Cursor
from matplotlib import cm
from matplotlib.widgets import RadioButtons, Slider
from radio_camera.lib.spectrogram_reader import reader
from BasicView import BasicView, plt


class View(object):
    def __init__(self):
        self.__config = Config("radio_camera")
        self.__ax = {}
        self.__im = {}

    def __gamma_slider_changed(self, val, im, vmin, vmax):
        im.set_norm(cm.colors.PowerNorm(gamma=val, vmin=vmin, vmax=vmax))
        self.__fig.canvas.draw_idle()

    def __main_view(self, properties=[], frequencies=[], spectrogram=[]):
        vmax = np.max(spectrogram["magnitude"])
        vmin = np.min(spectrogram["magnitude"])
        power_spectrogram = np.power(10, (spectrogram["magnitude"] - 30) / 10)
        t_power_spectrogram = np.sum(power_spectrogram, axis=0) * 1000
        f_power_spectrogram = np.log10(np.sum(power_spectrogram, axis=1) * 1000)

        mosaic = [
            ["spectrogram", "colorbar", "f_proj", "t_power"],
            ["t_proj", "band_selection", "band_selection", "f_power"],
            ["t_proj", "gamma_setting_slider", "gamma_setting_slider", "f_power"],
            [None, None, None, None],
        ]
        self.__fig, self.__ax = BasicView.basic_view(
            "Radio camera",
            mosaic=mosaic,
            width_ratios=[15, 1, 3, 15],
            height_ratios=[6, 2, 0.1, 0.5],
        )

        self.__im["spectrogram"] = self.__ax["spectrogram"].imshow(
            X=spectrogram["magnitude"],
            norm=cm.colors.PowerNorm(
                gamma=self.__config.data["gamma"], vmin=vmin, vmax=vmax
            ),
            cmap=self.__config.data["cmap"],
            aspect="auto",
            origin="lower",
            extent=[
                min(spectrogram["relative_time"]),
                max(spectrogram["relative_time"]),
                min(spectrogram["frequency"]) / 1000000,
                max(spectrogram["frequency"]) / 1000000,
            ],
        )
        self.__ax["spectrogram"].set_xlim(self.__im["spectrogram"].get_extent()[0:2])
        self.__ax["spectrogram"].set_ylim(self.__im["spectrogram"].get_extent()[2:4])

        lims = Lims(self.__im)
        self.__ax["spectrogram"].callbacks.connect("xlim_changed", lims.on_xlim_changed)
        self.__ax["spectrogram"].callbacks.connect("ylim_changed", lims.on_ylim_changed)
        self.__ax["spectrogram"].set_title("Spectrogram")
        self.__ax["spectrogram"].set_xlabel("Relative time from start [ms]")
        self.__ax["spectrogram"].set_ylabel("Frequency [MHz]")
        BasicView.set_grid(self.__ax["spectrogram"])

        self.__fig.colorbar(self.__im["spectrogram"], cax=self.__ax["colorbar"])

        (self.__im["t_proj"],) = self.__ax["t_proj"].plot([], [])
        self.__ax["t_proj"].set_title("Time projection")
        self.__ax["t_proj"].set_xlabel("Relative time from start [ms]")
        self.__ax["t_proj"].set_ylabel(
            f"Magnitude [{spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["t_proj"].set_xlim(self.__ax["spectrogram"].get_xlim()[0:2])
        self.__ax["t_proj"].margins(x=0)
        BasicView.set_grid(self.__ax["t_proj"])

        (self.__im["f_proj"],) = self.__ax["f_proj"].plot([], [])
        self.__ax["f_proj"].set_title("Frequency projection")
        self.__ax["f_proj"].set_xlabel("Frequency [MHz]")
        self.__ax["f_proj"].set_ylabel(
            f"Magnitude [{spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["f_proj"].set_ylim(self.__ax["spectrogram"].get_ylim()[0:2])
        self.__ax["f_proj"].margins(y=0)
        self.__ax["f_proj"].is_rotated = True
        BasicView.set_grid(self.__ax["f_proj"])

        self.__gamma_slider = Slider(
            ax=self.__ax["gamma_setting_slider"],
            label="Gamma",
            valmin=0,
            valmax=1,
            valinit=self.__im["spectrogram"].norm.gamma,
        )
        self.__gamma_slider.on_changed(
            (
                lambda event: self.__gamma_slider_changed(
                    event, self.__im["spectrogram"], vmin, vmax
                )
            )
        )

        self.__ax["band_selection"].set_title("Band [MHz-MHz]")
        self.__band_selection_radiobuttons = RadioButtons(
            ax=self.__ax["band_selection"],
            radio_props={"s": [64] * len(self.__config.data["bands"])},
            labels=list(
                map(
                    lambda x: f"{x} {self.__config.data['bands'][x]}",
                    self.__config.data["bands"].keys(),
                )
            ),
        )

        (self.__im["t_power"],) = self.__ax["t_power"].plot(
            np.linspace(
                min(spectrogram["relative_time"]),
                max(spectrogram["relative_time"]),
                num=len(t_power_spectrogram),
            ),
            t_power_spectrogram,
        )
        self.__ax["t_power"].set_title("Time power")
        self.__ax["t_power"].set_xlabel("Relative time from start [ms]")
        self.__ax["t_power"].set_ylabel("Magnitude [µW]")
        BasicView.set_grid(self.__ax["t_power"])

        (self.__im["f_power"],) = self.__ax["f_power"].plot(
            np.linspace(
                min(spectrogram["frequency"] / 1000000),
                max(spectrogram["frequency"] / 1000000),
                num=len(f_power_spectrogram),
            ),
            f_power_spectrogram,
        )
        self.__ax["f_power"].set_title("Frequency power")
        self.__ax["f_power"].set_xlabel("Frequency [MHz]")
        self.__ax["f_power"].set_ylabel("Magnitude [log10(µW)]")
        BasicView.set_grid(self.__ax["f_power"])

        self.__cursor = Cursor(self.__ax, self.__im)
        plt.connect("button_press_event", self.__cursor.button_press_event)

    def view(self):
        filename = ""
        if "filename" in self.__config.data:
            if self.__config.data["filename"]:
                if os.path.isfile(self.__config.data["filename"]):
                    filename = self.__config.data["filename"]

        if not filename:
            filename = BasicView.basic_view_file_dialog(
                "Radio camera", "Select a spectrogram file"
            )

        if filename:
            pr, fr, sp = reader(filename, self.__config)
            self.__main_view(properties=pr, frequencies=fr, spectrogram=sp)
        else:
            self.__main_view()

        plt.show(block=True)
