import os
import numpy as np
import spectrogram
import basic_view
from viewer.Api import Api
from viewer.Lims import Lims
from viewer.Cursor import Cursor


class View(object):
    def __init__(self, conf):
        self.__conf = conf
        self.__ax = {}
        self.__im = {}
        self.__api = Api()

    def __gamma_slider_changed(self, val):
        self.__im["spectrogram"].set_norm(
            basic_view.cm.colors.PowerNorm(
                gamma=val,
                vmin=np.min(self.__spectrogram["magnitude"]),
                vmax=np.max(self.__spectrogram["magnitude"]),
            )
        )
        self.__fig.canvas.draw_idle()

    def __clear_all(self):
        self.__properties = None
        self.__frequencies = None
        self.__spectrogram = None
        self.__filename = None
        self.__clear_axes()

    def __clear_axes(self):
        basic_view.cla_leaving_attributes(self.__ax["spectrogram"])
        basic_view.cla_leaving_attributes(self.__ax["t_proj"])
        basic_view.cla_leaving_attributes(self.__ax["colorbar"])
        basic_view.cla_leaving_attributes(self.__ax["f_proj"])
        basic_view.cla_leaving_attributes(self.__ax["f_power"])
        basic_view.cla_leaving_attributes(self.__ax["t_power"])
        basic_view.set_title(fig=self.__fig)

    def __add(self, arr):
        print("ciao")
        return False

    def __populate(self, x):
        lo = float(
            self.__conf["global"]["lo"][self.__lo_radiobuttons.index_selected]["value"]
        )
        power_spectrogram = np.power(10, (self.__spectrogram["magnitude"] - 30) / 10)
        t_power_spectrogram = np.sum(power_spectrogram, axis=0) * 1000
        f_power_spectrogram = np.log10(np.sum(power_spectrogram, axis=1) * 1000)

        self.__clear_axes()

        # # 1. normalization magnitudes in the range [0; 255]
        # norm_magn = (
        #     255
        #     * (self.__spectrogram["magnitude"] - self.__spectrogram["magnitude"].min())
        #     / (
        #         self.__spectrogram["magnitude"].max()
        #         - self.__spectrogram["magnitude"].min()
        #     )
        # )

        # # 2. map radio frequencies to light frequencies
        # min_light_freq = 380 * 10**12
        # max_light_freq = 750 * 10**12
        # false_freqs = min_light_freq + (max_light_freq - min_light_freq) * (
        #     self.__spectrogram["frequency"] - self.__spectrogram["frequency"].min()
        # ) / (
        #     self.__spectrogram["frequency"].max()
        #     - self.__spectrogram["frequency"].min()
        # )

        # # 3. map frequencies to RGB with normalized magnitudes
        # false_mag = [
        #     [wavelen2rgb(freq_to_nm(false_freqs[ids]), int(el)) for el in els]
        #     for ids, els in enumerate(norm_magn)
        # ]

        self.__im["spectrogram"] = self.__ax["spectrogram"].imshow(
            # false_mag,
            X=self.__spectrogram["magnitude"],
            norm=basic_view.cm.colors.PowerNorm(
                gamma=self.__conf["gamma"],
                vmin=np.min(self.__spectrogram["magnitude"]),
                vmax=np.max(self.__spectrogram["magnitude"]),
            ),
            cmap=self.__conf["cmap"],
            aspect="auto",
            origin="lower",
            extent=[
                lo + min(self.__spectrogram["relative_time"]),
                lo + max(self.__spectrogram["relative_time"]),
                lo + min(self.__spectrogram["frequency"]) / 1000000,
                lo + max(self.__spectrogram["frequency"]) / 1000000,
            ],
        )
        self.__ax["spectrogram"].set_xlim(self.__im["spectrogram"].get_extent()[0:2])
        self.__ax["spectrogram"].set_ylim(self.__im["spectrogram"].get_extent()[2:4])

        lims = Lims(self.__im)
        self.__ax["spectrogram"].callbacks.connect("xlim_changed", lims.on_xlim_changed)
        self.__ax["spectrogram"].callbacks.connect("ylim_changed", lims.on_ylim_changed)
        self.__ax["spectrogram"].set_xlabel("Relative time from start [ms]")
        self.__ax["spectrogram"].set_ylabel("Frequency [MHz]")
        basic_view.set_grid(self.__ax["spectrogram"])

        self.__fig.colorbar(self.__im["spectrogram"], cax=self.__ax["colorbar"])

        (self.__im["t_proj"],) = self.__ax["t_proj"].plot([], [])
        self.__ax["t_proj"].set_xlabel("Relative time from start [ms]")
        self.__ax["t_proj"].set_ylabel(
            f"Magnitude [{self.__spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["t_proj"].set_xlim(self.__ax["spectrogram"].get_xlim()[0:2])
        self.__ax["t_proj"].margins(x=0)
        basic_view.set_grid(self.__ax["t_proj"])

        (self.__im["f_proj"],) = self.__ax["f_proj"].plot([], [])
        self.__ax["f_proj"].set_xlabel("Frequency [MHz]")
        self.__ax["f_proj"].set_ylabel(
            f"Magnitude [{self.__spectrogram["um"]["magnitude"][1]}]"
        )
        self.__ax["f_proj"].set_ylim(self.__ax["spectrogram"].get_ylim()[0:2])
        self.__ax["f_proj"].margins(y=0)
        self.__ax["f_proj"].is_rotated = True
        basic_view.set_grid(self.__ax["f_proj"])

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
        basic_view.set_grid(self.__ax["t_power"])

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
        basic_view.set_grid(self.__ax["f_power"])

        self.__cursor = Cursor(self.__ax, self.__im)
        basic_view.connect("button_press_event", self.__cursor.button_press_event)

        basic_view.set_title(
            fig=self.__fig, subtitles=[os.path.basename(self.__filename)]
        )

    def __load(self, filename):
        if filename:
            if not os.path.isfile(filename):
                basic_view.show_message(
                    self.__conf["name"],
                    f"File {filename} is not readable or incorrectly formatted",
                    icon=2,
                )
            else:
                props, freqs, specgram = spectrogram.reader(filename, self.__conf)
                if props is None or freqs is None or specgram is None:
                    basic_view.show_message(
                        self.__conf["name"],
                        f"File {filename} is not readable or incorrectly formatted",
                        icon=2,
                    )
                else:
                    self.__properties = props
                    self.__frequencies = freqs
                    self.__spectrogram = specgram
                    self.__filename = filename

                    self.__lo_radiobuttons = basic_view.RadioButtons(
                        ax=self.__ax["lo"],
                        radio_props={"s": [64] * len(self.__conf["global"]["lo"])},
                        labels=list(
                            map(
                                lambda x: f"{x["value"]} {x["band"] if "band" in x else ""}",
                                self.__conf["global"]["lo"],
                            )
                        ),
                    )
                    self.__lo_radiobuttons.on_clicked(self.__populate)

                    self.__gamma_slider = basic_view.Slider(
                        ax=self.__ax["gamma_slider"],
                        label="Gamma",
                        valmin=0,
                        valmax=1,
                        valinit=self.__conf["gamma"],
                    )
                    self.__gamma_slider.on_changed(
                        lambda x: self.__gamma_slider_changed(x)
                    )

                    self.__populate(None)

        basic_view.refresh()

    def __viewer_setup(self):
        self.__clear_all()
        basic_view.set_title(fig=self.__fig, subtitles=["Waiting for slices..."])

    def view(self):
        mosaic = basic_view.generate_array(50, 50)
        buttons = [
            "viewer",
            "controller",
            None,
            None,
            None,
            None,
            None,
            "clear",
            "load_csv",
            "info",
        ]
        basic_view.fill_row_with_array(mosaic, (1, 1), (50, 2), buttons)

        # first column
        basic_view.fill_with_string(mosaic, (1, 2), (25, 30), "spectrogram", (1, 2))
        basic_view.fill_with_string(mosaic, (1, 30), (25, 49), "t_proj", (1, 5))

        # second column
        basic_view.fill_with_string(mosaic, (25, 2), (27, 30), "colorbar", (1, 2))
        basic_view.fill_with_string(mosaic, (27, 2), (38, 30), "f_proj", (4, 2))
        basic_view.fill_with_string(mosaic, (25, 30), (38, 45), "lo", (1, 5))
        basic_view.fill_with_string(mosaic, (25, 45), (38, 49), "gamma_slider", (3, 2))

        # third column
        basic_view.fill_with_string(mosaic, (38, 2), (50, 27), "f_power", (3, 2))
        basic_view.fill_with_string(mosaic, (38, 27), (50, 49), "t_power", (3, 5))

        self.__fig, self.__ax = basic_view.create(
            self.__conf["name"], mosaic, "icons/whistle_of_wind.png"
        )

        basic_view.buttons_frame(self, self.__ax, self.__conf["package"])

        self.__ax["spectrogram"].set_title("Spectrogram")
        self.__ax["t_proj"].set_title("Time projection")
        self.__ax["f_proj"].set_title("Frequency projection")
        self.__ax["f_power"].set_title("Frequency power")
        self.__ax["t_power"].set_title("Time power")
        self.__ax["lo"].set_title("LO freq [MHz]")

        self.__clear_button = basic_view.Button(ax=self.__ax["clear"], label="Clear")
        self.__clear_button.on_clicked(lambda x: self.__clear_all())

        def load_csv_button_click():
            file = basic_view.file_dialog(
                title=self.__conf["name"],
                message="Load CSV",
                filter="CSV files (*.csv)",
            )

            if file:
                self.__load(filename=file)

        self.__load_csv_button = basic_view.Button(
            ax=self.__ax["load_csv"], label="Load CSV"
        )
        self.__load_csv_button.on_clicked(lambda x: load_csv_button_click())

        self.__info_button = basic_view.Button(ax=self.__ax["info"], label="Info")
        self.__info_button.on_clicked(
            lambda x: basic_view.table(
                title=f"{os.path.basename(self.__filename)} info",
                dataframe=self.__properties,
            )
        )

        Api._viewer_setup_callback = self.__viewer_setup
        Api._viewer_add_callback = self.__add
        self.__api.run(port=self.__conf["global"]["port"])

        self.__clear_all()
        file = self.__conf["filename"] if "filename" in self.__conf else None
        self.__load(filename=file)

        basic_view.show()
