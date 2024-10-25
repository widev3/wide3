import os
import utils
import numpy as np
from radio_camera.Lims import Lims
from radio_camera.Cursor import Cursor
from radio_camera.lib.spectrogram import reader
from BasicView import BasicView, cm, RadioButtons, Button, Slider, plt
from Mosaic import Mosaic


class View(object):
    def __init__(self, config):
        if not config:
            config = {}
            config["package"] = __package__
            config["name"] = utils.package_to_name(__package__)
            config["bands"] = {}
            config["bands"]["A"] = [10, 12]
            config["separator"] = ","
            config["gamma"] = 0.3
            config["cmap"] = "magma"

        self.__config = config
        self.__ax = {}
        self.__im = {}

    def __gamma_slider_changed(self, val, im, vmin, vmax):
        im.set_norm(cm.colors.PowerNorm(gamma=val, vmin=vmin, vmax=vmax))
        self.__fig.canvas.draw_idle()

    def __populate(self, properties=None, frequencies=None, spectrogram=None):
        vmax = np.max(spectrogram["magnitude"])
        vmin = np.min(spectrogram["magnitude"])
        power_spectrogram = np.power(10, (spectrogram["magnitude"] - 30) / 10)
        t_power_spectrogram = np.sum(power_spectrogram, axis=0) * 1000
        f_power_spectrogram = np.log10(np.sum(power_spectrogram, axis=1) * 1000)

        self.__im["spectrogram"] = self.__ax["spectrogram"].imshow(
            X=spectrogram["magnitude"],
            norm=cm.colors.PowerNorm(
                gamma=self.__config["gamma"], vmin=vmin, vmax=vmax
            ),
            cmap=self.__config["cmap"],
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
        self.__ax["spectrogram"].set_xlabel("Relative time from start [ms]")
        self.__ax["spectrogram"].set_ylabel("Frequency [MHz]")
        BasicView.set_grid(self.__ax["spectrogram"])

        self.__fig.colorbar(self.__im["spectrogram"], cax=self.__ax["colorbar"])

        (self.__im["t_proj"],) = self.__ax["t_proj"].plot([], [])
        self.__ax["t_proj"].set_xlabel("Relative time from start [ms]")
        self.__ax["t_proj"].set_ylabel(
            f"Magnitude [{spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["t_proj"].set_xlim(self.__ax["spectrogram"].get_xlim()[0:2])
        self.__ax["t_proj"].margins(x=0)
        BasicView.set_grid(self.__ax["t_proj"])

        (self.__im["f_proj"],) = self.__ax["f_proj"].plot([], [])
        self.__ax["f_proj"].set_xlabel("Frequency [MHz]")
        self.__ax["f_proj"].set_ylabel(
            f"Magnitude [{spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["f_proj"].set_ylim(self.__ax["spectrogram"].get_ylim()[0:2])
        self.__ax["f_proj"].margins(y=0)
        self.__ax["f_proj"].is_rotated = True
        BasicView.set_grid(self.__ax["f_proj"])

        self.__gamma_slider = Slider(
            ax=self.__ax["gamma_slider"],
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

        (self.__im["t_power"],) = self.__ax["t_power"].plot(
            np.linspace(
                min(spectrogram["relative_time"]),
                max(spectrogram["relative_time"]),
                num=len(t_power_spectrogram),
            ),
            t_power_spectrogram,
        )
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
        self.__ax["f_power"].set_xlabel("Frequency [MHz]")
        self.__ax["f_power"].set_ylabel("Magnitude [log10(µW)]")
        BasicView.set_grid(self.__ax["f_power"])

        self.__cursor = Cursor(self.__ax, self.__im)
        BasicView.connect("button_press_event", self.__cursor.button_press_event)

    def __draw(self, filename=None):
        if not filename and "filename" in self.__config:
            if self.__config["filename"]:
                filename = self.__config["filename"]

        properties = None
        frequencies = None
        spectrogram = None
        if filename and os.path.isfile(filename):
            properties, frequencies, spectrogram = reader(filename, self.__config)
            if properties is None or frequencies is None or spectrogram is None:
                BasicView.basic_view_show_message(
                    self.__config["name"],
                    f"Current file {filename} is not readable or incorrectly formatted",
                    2,
                )

        if properties is None or frequencies is None or spectrogram is None:
            return

        if len(properties) == 0 or len(frequencies) == 0 or len(spectrogram) == 0:
            return

        self.__populate(properties, frequencies, spectrogram)
        BasicView.refresh()

    def view(self, filename=None):
        mosaic = Mosaic.generate_array(50, 50)
        buttons = ["load_csv", None, None, None, None, None]
        Mosaic.fill_row_with_array(mosaic, (1, 1), (50, 2), buttons)

        # first column
        Mosaic.fill_with_string(mosaic, (1, 2), (25, 30), "spectrogram", (1, 2))
        Mosaic.fill_with_string(mosaic, (1, 30), (25, 50), "t_proj", (1, 5))

        # second column
        Mosaic.fill_with_string(mosaic, (25, 2), (27, 30), "colorbar", (1, 2))
        Mosaic.fill_with_string(mosaic, (27, 2), (38, 30), "f_proj", (4, 2))
        Mosaic.fill_with_string(mosaic, (25, 30), (38, 45), "bands", (1, 5))
        Mosaic.fill_with_string(mosaic, (25, 45), (38, 50), "gamma_slider", (3, 2))

        # third column
        Mosaic.fill_with_string(mosaic, (38, 2), (50, 27), "f_power", (3, 2))
        Mosaic.fill_with_string(mosaic, (38, 27), (50, 50), "t_power", (3, 5))

        self.__fig, self.__ax = BasicView.basic_view(
            self.__config["name"], mosaic=mosaic
        )

        self.__ax["spectrogram"].set_title("Spectrogram")
        self.__ax["t_proj"].set_title("Time projection")
        self.__ax["f_proj"].set_title("Frequency projection")
        self.__ax["f_power"].set_title("Frequency power")
        self.__ax["t_power"].set_title("Time power")

        self.__ax["bands"].set_title("Band [MHz-MHz]")
        self.__bands_radiobuttons = RadioButtons(
            ax=self.__ax["bands"],
            radio_props={"s": [64] * len(self.__config["bands"])},
            labels=list(
                map(
                    lambda x: f"{x} {self.__config["bands"][x]}",
                    self.__config["bands"].keys(),
                )
            ),
        )

        self.__load_csv_button = Button(ax=self.__ax["load_csv"], label="Load CSV")
        self.__load_csv_button.on_clicked(
            lambda x: self.__draw(
                BasicView.basic_view_file_dialog(self.__config["name"], "Load CSV")
            )
        )

        self.__draw(filename)

        BasicView.show()
