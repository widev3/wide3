import os
import numpy as np
from radio_camera.Lims import Lims
from radio_camera.Cursor import Cursor
from radio_camera.lib.spectrogram import reader
from BasicView import BasicView, cm, RadioButtons, Button, Slider


class View(object):
    def __init__(self, conf):
        self.__conf = conf
        self.__ax = {}
        self.__im = {}

    def __gamma_slider_changed(self, val, im, vmin, vmax):
        im.set_norm(cm.colors.PowerNorm(gamma=val, vmin=vmin, vmax=vmax))
        self.__fig.canvas.draw_idle()

    def __clear_axes(self):
        self.__filename = None
        self.__lo = 0
        BasicView.cla_leaving_attributes(self.__ax["spectrogram"])
        BasicView.cla_leaving_attributes(self.__ax["t_proj"])
        BasicView.cla_leaving_attributes(self.__ax["colorbar"])
        BasicView.cla_leaving_attributes(self.__ax["f_proj"])
        BasicView.cla_leaving_attributes(self.__ax["lo"])
        BasicView.cla_leaving_attributes(self.__ax["gamma_slider"])
        BasicView.cla_leaving_attributes(self.__ax["f_power"])
        BasicView.cla_leaving_attributes(self.__ax["t_power"])
        BasicView.set_title(fig=self.__fig, subtitle=None)

    def __populate(self):
        self.__clear_axes()

        vmax = np.max(self.__spectrogram["magnitude"])
        vmin = np.min(self.__spectrogram["magnitude"])
        power_spectrogram = np.power(10, (self.__spectrogram["magnitude"] - 30) / 10)
        t_power_spectrogram = np.sum(power_spectrogram, axis=0) * 1000
        f_power_spectrogram = np.log10(np.sum(power_spectrogram, axis=1) * 1000)

        def switch_lo(freq):
            self.__lo = freq
            self.__populate()

        self.__lo_radiobuttons = RadioButtons(
            ax=self.__ax["lo"],
            radio_props={"s": [64] * len(self.__conf["lo"])},
            labels=list(
                map(
                    lambda x: f"{x["value"]} {x["band"] if "band" in x else ""}",
                    self.__conf["lo"],
                )
            ),
        )
        self.__lo_radiobuttons.on_clicked(lambda x: switch_lo(float(x.split(" ")[0])))
        self.__lo = float(
            self.__conf["lo"][self.__lo_radiobuttons.index_selected]["value"]
        )

        self.__im["spectrogram"] = self.__ax["spectrogram"].imshow(
            X=self.__spectrogram["magnitude"],
            norm=cm.colors.PowerNorm(gamma=self.__conf["gamma"], vmin=vmin, vmax=vmax),
            cmap=self.__conf["cmap"],
            aspect="auto",
            origin="lower",
            extent=[
                self.__lo + min(self.__spectrogram["relative_time"]),
                self.__lo + max(self.__spectrogram["relative_time"]),
                self.__lo + min(self.__spectrogram["frequency"]) / 1000000,
                self.__lo + max(self.__spectrogram["frequency"]) / 1000000,
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
            f"Magnitude [{self.__spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["t_proj"].set_xlim(self.__ax["spectrogram"].get_xlim()[0:2])
        self.__ax["t_proj"].margins(x=0)
        BasicView.set_grid(self.__ax["t_proj"])

        (self.__im["f_proj"],) = self.__ax["f_proj"].plot([], [])
        self.__ax["f_proj"].set_xlabel("Frequency [MHz]")
        self.__ax["f_proj"].set_ylabel(
            f"Magnitude [{self.__spectrogram["um"]["magnitude"][1]}]"
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
                self.__im["spectrogram"].get_extent()[0],
                self.__im["spectrogram"].get_extent()[1],
                num=len(t_power_spectrogram),
            ),
            t_power_spectrogram,
        )
        self.__ax["t_power"].set_xlabel("Relative time from start [ms]")
        self.__ax["t_power"].set_ylabel("Magnitude [µW]")
        BasicView.set_grid(self.__ax["t_power"])

        (self.__im["f_power"],) = self.__ax["f_power"].plot(
            np.linspace(
                self.__im["spectrogram"].get_extent()[2],
                self.__im["spectrogram"].get_extent()[3],
                num=len(f_power_spectrogram),
            ),
            f_power_spectrogram,
        )
        self.__ax["f_power"].set_xlabel("Frequency [MHz]")
        self.__ax["f_power"].set_ylabel("Magnitude [log10(µW)]")
        BasicView.set_grid(self.__ax["f_power"])

        self.__cursor = Cursor(self.__ax, self.__im)
        BasicView.connect("button_press_event", self.__cursor.button_press_event)

    def __load(self, filename):
        self.__properties = None
        self.__frequencies = None
        self.__spectrogram = None
        if filename:
            if not os.path.isfile(filename):
                BasicView.show_message(
                    self.__conf["name"],
                    f"Current file {filename} is not readable or incorrectly formatted",
                    2,
                )
            else:
                self.__properties, self.__frequencies, self.__spectrogram = reader(
                    filename, self.__conf
                )
                if (
                    self.__properties is None
                    or self.__frequencies is None
                    or self.__spectrogram is None
                ):
                    BasicView.show_message(
                        self.__conf["name"],
                        f"Current file {filename} is not readable or incorrectly formatted",
                        2,
                    )
                else:
                    self.__filename = filename
                    self.__populate()
        else:
            self.__clear_axes()

        BasicView.refresh()

    def view(self):
        mosaic = BasicView.generate_array(50, 50)
        buttons = [
            "radio_camera",
            "mount_control",
            None,
            None,
            None,
            None,
            None,
            None,
            "clear",
            "load_csv",
        ]
        BasicView.fill_row_with_array(mosaic, (1, 1), (50, 2), buttons)

        # first column
        BasicView.fill_with_string(mosaic, (1, 2), (25, 30), "spectrogram", (1, 2))
        BasicView.fill_with_string(mosaic, (1, 30), (25, 49), "t_proj", (1, 5))

        # second column
        BasicView.fill_with_string(mosaic, (25, 2), (27, 30), "colorbar", (1, 2))
        BasicView.fill_with_string(mosaic, (27, 2), (38, 30), "f_proj", (4, 2))
        BasicView.fill_with_string(mosaic, (25, 30), (38, 45), "lo", (1, 5))
        BasicView.fill_with_string(mosaic, (25, 45), (38, 49), "gamma_slider", (3, 2))

        # third column
        BasicView.fill_with_string(mosaic, (38, 2), (50, 27), "f_power", (3, 2))
        BasicView.fill_with_string(mosaic, (38, 27), (50, 49), "t_power", (3, 5))

        self.__fig, self.__ax = BasicView.create(self.__conf["name"], mosaic)

        BasicView.buttons_frame(self, self.__ax, self.__conf["package"])

        self.__ax["spectrogram"].set_title("Spectrogram")
        self.__ax["t_proj"].set_title("Time projection")
        self.__ax["f_proj"].set_title("Frequency projection")
        self.__ax["f_power"].set_title("Frequency power")
        self.__ax["t_power"].set_title("Time power")
        self.__ax["lo"].set_title("LO freq [MHz]")

        self.__clear_button = Button(ax=self.__ax["clear"], label="Clear")
        self.__clear_button.on_clicked(lambda x: self.__load(filename=None))

        def load():
            file = BasicView.file_dialog(
                title=self.__conf["name"],
                message="Load CSV",
                filter="csv Files (*.csv)",
            )
            if file:
                self.__load(filename=file)

        self.__load_csv_button = Button(ax=self.__ax["load_csv"], label="Load CSV")
        self.__load_csv_button.on_clicked(lambda x: load())

        self.__load(
            self.__conf["filename"]
            if "filename" in self.__conf and self.__conf["filename"]
            else None
        )

        BasicView.show()
