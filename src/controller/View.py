import sys
import numpy as np
import basic_view
import traceback
from datetime import datetime
from viewer.Lims import Lims
from viewer.Cursor import Cursor
from RsInstrument import RsInstrument


class View(object):
    def __init__(self, conf):
        self.__conf = conf
        self.__ax = {}
        self.__im = {}
        self.__instr = None

    def __gamma_slider_changed(self, val, im, vmin, vmax):
        im.set_norm(basic_view.cm.colors.PowerNorm(gamma=val, vmin=vmin, vmax=vmax))
        self.__fig.canvas.draw_idle()

    def __clear_axes(self):
        self.__lo = 0
        basic_view.cla_leaving_attributes(self.__ax["spectrogram"])
        basic_view.cla_leaving_attributes(self.__ax["t_proj"])
        basic_view.cla_leaving_attributes(self.__ax["colorbar"])
        basic_view.cla_leaving_attributes(self.__ax["f_proj"])
        basic_view.cla_leaving_attributes(self.__ax["lo"])
        basic_view.cla_leaving_attributes(self.__ax["gamma_slider"])
        basic_view.cla_leaving_attributes(self.__ax["f_power"])
        basic_view.cla_leaving_attributes(self.__ax["t_power"])
        basic_view.set_title(fig=self.__fig, subtitles=[])

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

        self.__lo_radiobuttons = basic_view.RadioButtons(
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
            norm=basic_view.cm.colors.PowerNorm(
                gamma=self.__conf["gamma"], vmin=vmin, vmax=vmax
            ),
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

        self.__gamma_slider = basic_view.Slider(
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

    def __disconnect_sa(self, x=None):
        try:
            if self.__instr and self.__instr.is_connection_active:
                self.__instr.close()
                self.__instr = None

            self.__connect_sa_button = basic_view.Button(
                ax=self.__ax["connect_sa"], label="Connect SA"
            )
            self.__connect_sa_button.on_clicked(lambda x: self.__connect_sa(instr=None))
        except:
            basic_view.show_message(
                self.__conf["name"],
                f"Error during disconnection to device {self.__instr}:\n{traceback.format_exc()}",
                icon=3,
            )

    def __connect_sa(self, instr):
        try:
            key = instr
            instr_list = RsInstrument.list_resources("?*")
            if instr_list:
                if not key and len(instr_list) == 1:
                    key = instr_list[0]
                elif (not key) or (key not in instr_list):
                    value, index, key = basic_view.checkbox_list(
                        self.__conf["name"],
                        "Select a backend device",
                        items_key=instr_list,
                        items_value=instr_list,
                        single=True,
                    )
            else:
                return basic_view.show_message(
                    self.__conf["name"],
                    f"No instrument available",
                    icon=2,
                )

            self.__disconnect_sa()
            self.__instr = RsInstrument(key, id_query=True, reset=True)
            idn = self.__instr.query_str("*IDN?")

            now = datetime.now()
            self.__instr.write("SYST:BEEP:KEY:VOL 0")
            self.__instr.write("SYST:BEEP:POV ON")
            self.__instr.write("SYST:BEEP:VOL 1")
            self.__instr.write("SYST:DISP:UPD ON")
            self.__instr.write(f"SYST:DATE {now.year},{now.month},{now.day}")
            self.__instr.write(f"SYST:TIME {now.hour},{now.minute},{now.second}")
            self.__instr.write("SYST:TZON 01,00")
            self.__instr.write("UNIT:LENG MET")
            self.__instr.write("INST:SEL SAN")
            self.__instr.write("UNIT:POW W")

            self.__ax["connect_sa"].cla()
            self.__connect_sa_button = basic_view.Button(
                ax=self.__ax["connect_sa"], label="Disconnect SA"
            )
            self.__connect_sa_button.on_clicked(self.__disconnect_sa)

            self.__ax["record"].cla()
            self.__record_button = basic_view.Button(
                ax=self.__ax["record"], label="Start record"
            )
            self.__record_button.on_clicked(self.__start_record)

            basic_view.set_title(fig=self.__fig, subtitles=[key])
            basic_view.show_message(
                self.__conf["name"],
                f"""Device {key} is connected!
IDN:\t{idn}
Driver version:\t{self.__instr.driver_version}
Visa manufacturer:\t{self.__instr.visa_manufacturer}
Instrument full name:\t{self.__instr.full_instrument_model_name}
Instrument options:\t{",".join(self.__instr.instrument_options)}""",
                icon=1,
            )
        except:
            basic_view.show_message(
                self.__conf["name"],
                f"Error during connection device {value}:\n{traceback.format_exc()}",
                icon=3,
            )

        basic_view.refresh()

    def __stop_record(self, x):
        self.__ax["record"].cla()
        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Start record"
        )
        self.__record_button.on_clicked(self.__start_record)

    def __start_record(self, x):
        self.__ax["record"].cla()
        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Stop record"
        )
        self.__record_button.on_clicked(self.__stop_record)

    def __instr_write(self, x=None):
        freq = float(self.__central_text_box.text) * 10**6
        span = float(self.__span_text_box.text) * 10**6
        sweep = float(self.__sweep_text_box.text) * 10**-3
        self.__instr.write(f"SENS:FREQ:CENT {freq}") if self.__instr else None
        self.__instr.write(f"SENS:FREQ:SPAN {span}") if self.__instr else None
        self.__instr.write(f"SENS:SWE:TIME {sweep}") if self.__instr else None

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
            None,
            "connect_sa",
            "record",
        ]
        basic_view.fill_row_with_array(mosaic, (1, 1), (50, 2), buttons)

        # first column
        basic_view.fill_with_string(mosaic, (1, 2), (5, 6), "central", (0, 3))
        basic_view.fill_with_string(mosaic, (1, 7), (5, 8), "span", (0, 0))
        basic_view.fill_with_string(mosaic, (1, 9), (5, 10), "sweep", (0, 0))
        basic_view.fill_with_string(mosaic, (1, 11), (5, 12), "confirm", (0, 0))

        # second column
        basic_view.fill_with_string(mosaic, (6, 2), (25, 6), "central_slider", (0, 3))
        basic_view.fill_with_string(mosaic, (6, 7), (25, 8), "span_slider", (0, 0))
        basic_view.fill_with_string(mosaic, (6, 9), (25, 10), "sweep_slider", (0, 0))

        self.__fig, self.__ax = basic_view.create(self.__conf["name"], mosaic)

        basic_view.buttons_frame(self, self.__ax, self.__conf["package"])

        self.__connect_sa_button = basic_view.Button(
            ax=self.__ax["connect_sa"], label="Connect SA"
        )
        self.__connect_sa_button.on_clicked(lambda x: self.__connect_sa(instr=None))

        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Start record"
        )
        self.__record_button.on_clicked(lambda x: None)
        self.__record_button.color = "gray"
        self.__record_button.hovercolor = "gray"

        self.__central_text_box = basic_view.TextBox(
            ax=self.__ax["central"],
            label="Central\n[MHz]",
            textalignment="left",
        )
        self.__central_text_box.set_val(
            self.__conf["central"] if "central" in self.__conf else 0
        )

        self.__span_text_box = basic_view.TextBox(
            ax=self.__ax["span"],
            label="Span\n[MHz]",
            textalignment="left",
        )
        self.__span_text_box.set_val(
            self.__conf["span"] if "span" in self.__conf else 0
        )

        self.__sweep_text_box = basic_view.TextBox(
            ax=self.__ax["sweep"],
            label="Sweep\n[ms]",
            textalignment="left",
        )
        self.__sweep_text_box.set_val(
            self.__conf["sweep"] if "sweep" in self.__conf else 0
        )

        self.__confirm_button = basic_view.Button(
            ax=self.__ax["confirm"], label="Confirm"
        )
        self.__confirm_button.on_clicked(self.__instr_write)

        self.__central_slider = basic_view.Slider(
            ax=self.__ax["central_slider"],
            label=None,
            valmin=0,
            valmax=3000,
            valinit=float(self.__central_text_box.text),
        )
        self.__central_slider.on_changed(
            lambda x: self.__central_text_box.set_val(int(x))
        )

        self.__span_slider = basic_view.Slider(
            ax=self.__ax["span_slider"],
            label=None,
            valmin=0,
            valmax=1500,
            valinit=float(self.__span_text_box.text),
        )
        self.__span_slider.on_changed(lambda x: self.__span_text_box.set_val(int(x)))

        self.__sweep_slider = basic_view.Slider(
            ax=self.__ax["sweep_slider"],
            label=None,
            valmin=0,
            valmax=60000,
            valinit=float(self.__sweep_text_box.text),
        )
        self.__sweep_slider.on_changed(lambda x: self.__sweep_text_box.set_val(int(x)))

        def set_sliders_and_write(x):
            self.__central_slider.set_val(float(self.__central_text_box.text))
            self.__span_slider.set_val(float(self.__span_text_box.text))
            self.__sweep_slider.set_val(float(self.__sweep_text_box.text))
            sys.stdout.flush()
            if x.key == "enter":
                self.__instr_write()

        basic_view.connect("key_press_event", set_sliders_and_write)

        if "instrument" in self.__conf:
            self.__connect_sa(instr=self.__conf["instrument"])

        basic_view.show()
