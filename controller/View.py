import sys
import time
import queue
import datetime
import threading
import spectrogram
import numpy as np
import pandas as pd
import basic_view
import traceback
from utils import stof_locale
from RsInstrument import RsInstrument


class View(object):
    def __init__(self, conf):
        self.__conf = conf
        self.__ax = {}
        self.__record = False
        self.__instr = None
        self.__freq = None
        self.__span = None
        self.__sweep = None

    def __disconnect_instr(self, x=None):
        try:
            if self.__instr and self.__instr.is_connection_active:
                self.__instr.close()
                self.__instr = None

            self.__connect_sa_button = basic_view.Button(
                ax=self.__ax["connect_sa"], label="Connect SA"
            )
            self.__connect_sa_button.on_clicked(
                lambda x: self.__connect_instr(instr=None)
            )
        except:
            basic_view.show_message(
                self.__conf["name"],
                f"Error during disconnection to device {self.__instr}:\n{traceback.format_exc()}",
                icon=3,
            )

    def __connect_instr(self, instr):
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

            self.__disconnect_instr()
            self.__instr = RsInstrument(key, id_query=True, reset=True)
            idn = self.__instr_comm(cmd="*IDN?", case="query_str")

            now = datetime.datetime.now()
            self.__instr_comm("SYST:BEEP:KEY:VOL", 0)
            self.__instr_comm("SYST:BEEP:POV", "ON")
            self.__instr_comm("SYST:BEEP:VOL", 1)
            self.__instr_comm("SYST:DISP:UPD", "ON")
            self.__instr_comm("SYST:DATE", f"{now.year},{now.month},{now.day}")
            self.__instr_comm("SYST:TIME", f"{now.hour},{now.minute},{now.second}")
            self.__instr_comm("SYST:TZON", "01,00")
            self.__instr_comm("UNIT:LENG", "MET")
            self.__instr_comm("INST:SEL", "SAN")
            self.__instr_comm("UNIT:POW", "W")
            self.__instr_comm("INIT:CONT", "ON")

            self.__ax["connect_sa"].cla()
            self.__connect_sa_button = basic_view.Button(
                ax=self.__ax["connect_sa"], label="Disconnect SA"
            )
            self.__connect_sa_button.on_clicked(self.__disconnect_instr)

            self.__ax["record"].cla()
            self.__record_button = basic_view.Button(
                ax=self.__ax["record"], label="Start record"
            )
            self.__record_button.on_clicked(self.__start_record)

            self.__instr_update()

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

        self.__record = False
        self.__instr_comm("INIT:CONT", "ON")

    def __start_record(self, x):
        req(
            url=f"http://localhost:{self.__conf["global"]["port"]}/viewer/setup",
            method="get",
        )

        self.__ax["record"].cla()
        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Stop record"
        )
        self.__record_button.on_clicked(self.__stop_record)

        self.__output_file = (
            f"{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"
        )
        self.__instr_comm("INIT:CONT", "OFF")
        self.__record = True

    def __instr_comm(self, cmd=None, val=None, case=None):
        try:
            if not self.__instr:
                return False
            elif not case:
                return self.__instr.write(f"{cmd}{f" {val}" if val else ""}")
            elif not cmd and not val:
                return getattr(self.__instr, case)()
            elif cmd or val:
                return getattr(self.__instr, case)(f"{cmd}{f" {val}" if val else ""}")
        except:
            return False

    def __instr_update(self, x=None):
        self.__freq = stof_locale(self.__central_text_box.text) * 10**6
        self.__span = stof_locale(self.__span_text_box.text) * 10**6
        self.__sweep = stof_locale(self.__sweep_text_box.text) * 10**-3
        self.__instr_comm(cmd="SENS:FREQ:CENT", val=self.__freq)
        self.__instr_comm(cmd="SENS:FREQ:SPAN", val=self.__span)
        self.__instr_comm(cmd="SENS:SWE:TIME", val=self.__sweep)

    def view(self):
        mosaic = basic_view.generate_array(25, 25)
        buttons = [
            "viewer",
            "controller",
            None,
            None,
            "connect_sa",
            "record",
        ]
        basic_view.fill_row_with_array(mosaic, (1, 1), (25, 2), buttons)

        # first column
        basic_view.fill_with_string(mosaic, (1, 2), (5, 6), "central", (1, 3))
        basic_view.fill_with_string(mosaic, (1, 7), (5, 8), "span", (1, 0))
        basic_view.fill_with_string(mosaic, (1, 9), (5, 10), "sweep", (1, 0))
        basic_view.fill_with_string(mosaic, (1, 11), (5, 12), "confirm", (1, 0))
        basic_view.fill_with_string(mosaic, (15, 13), (25, 25), "lo", (1, 1))

        # second column
        basic_view.fill_with_string(mosaic, (6, 2), (22, 6), "central_slider", (0, 3))
        basic_view.fill_with_string(mosaic, (6, 7), (22, 8), "span_slider", (0, 0))
        basic_view.fill_with_string(mosaic, (6, 9), (22, 10), "sweep_slider", (0, 0))

        self.__fig, self.__ax = basic_view.create(
            self.__conf["name"],
            mosaic,
            icon="icons/control_camera_144dp_992B15_FILL0_wght400_GRAD0_opsz48.png",
            unwanted_buttons=None,
            size=(800, 500),
        )

        basic_view.buttons_frame(self, self.__ax, self.__conf["package"])

        def populate():
            lo = float(
                self.__conf["global"]["lo"][self.__lo_radiobuttons.index_selected][
                    "value"
                ]
            )
            print(lo)

        self.__ax["lo"].set_title("LO freq [MHz]")
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
        self.__lo_radiobuttons.on_clicked(populate)

        self.__connect_sa_button = basic_view.Button(
            ax=self.__ax["connect_sa"], label="Connect SA"
        )
        self.__connect_sa_button.on_clicked(lambda x: self.__connect_instr(instr=None))

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
            round(self.__conf["central"] if "central" in self.__conf else 0, 4)
        )

        self.__span_text_box = basic_view.TextBox(
            ax=self.__ax["span"],
            label="Span\n[MHz]",
            textalignment="left",
        )
        self.__span_text_box.set_val(
            round(self.__conf["span"] if "span" in self.__conf else 0, 4)
        )

        self.__sweep_text_box = basic_view.TextBox(
            ax=self.__ax["sweep"],
            label="Sweep\n[ms]",
            textalignment="left",
        )
        self.__sweep_text_box.set_val(
            round(self.__conf["sweep"] if "sweep" in self.__conf else 0, 4)
        )

        self.__confirm_button = basic_view.Button(
            ax=self.__ax["confirm"], label="Confirm"
        )
        self.__confirm_button.on_clicked(self.__instr_update)

        self.__central_slider = basic_view.Slider(
            ax=self.__ax["central_slider"],
            label=None,
            valmin=0,
            valmax=3000,
            valinit=stof_locale(self.__central_text_box.text),
        )
        self.__central_slider.on_changed(
            lambda x: self.__central_text_box.set_val(round(x, 4))
        )

        self.__span_slider = basic_view.Slider(
            ax=self.__ax["span_slider"],
            label=None,
            valmin=0,
            valmax=1500,
            valinit=float(self.__span_text_box.text),
        )
        self.__span_slider.on_changed(
            lambda x: self.__span_text_box.set_val(round(x, 4))
        )

        self.__sweep_slider = basic_view.Slider(
            ax=self.__ax["sweep_slider"],
            label=None,
            valmin=0,
            valmax=60000,
            valinit=float(self.__sweep_text_box.text),
        )
        self.__sweep_slider.on_changed(
            lambda x: self.__sweep_text_box.set_val(round(x, 4))
        )

        def set_sliders_and_write(x):
            if x.key == "enter":
                sys.stdout.flush()
                self.__central_slider.set_val(stof_locale(self.__central_text_box.text))
                self.__span_slider.set_val(stof_locale(self.__span_text_box.text))
                self.__sweep_slider.set_val(stof_locale(self.__sweep_text_box.text))
                self.__instr_update()

        basic_view.connect("key_press_event", set_sliders_and_write)

        slices_queue = queue.Queue()

        def background_instr():
            class Slice:
                def __init__(self, dt, slice):
                    self.datetime = dt.strftime("%H:%M:%S %d/%m/%Y")
                    self.timestamp = datetime.datetime.timestamp(dt)
                    self.slice = slice

            def time_slice(values, cent=None, span=None, start=None, stop=None):
                f_start = None
                f_stop = None
                if cent and span:
                    f_start = cent - span
                    f_stop = cent + span
                elif cent and start:
                    f_start = start
                    f_stop = 2 * start - cent
                elif cent and stop:
                    f_start = 2 * cent - stop
                    f_stop = stop
                elif span and start:
                    f_start = start
                    f_stop = start + 2 * span
                elif span and stop:
                    f_start = stop - 2 * span
                    f_stop = stop
                elif start and stop:
                    f_start = start
                    f_stop = stop

                frequencies = np.linspace(f_start, f_stop, len(values))
                frequencies = list(map(lambda x: float(x), frequencies))
                return dict(zip(frequencies, values))

            while True:
                time.sleep(self.__sweep / 3) if self.__sweep else time.sleep(0.1)
                if self.__record:
                    self.__instr_comm("INIT:IMM")
                    self.__instr_comm(case="query_opc")

                    data = self.__instr_comm(cmd="TRACE:DATA?", case="query_str")
                    if data:
                        values = [float(value) for value in data.split(",")]
                        slice = time_slice(values, cent=self.__freq, span=self.__span)
                        slices_queue.put(Slice(dt=datetime.datetime.now(), slice=slice))

        self.__thread_instr = threading.Thread(target=background_instr)
        self.__thread_instr.daemon = True
        self.__thread_instr.start()

        def background_api_client():
            df = {}
            total = 0
            while True:
                time.sleep(self.__sweep * 10) if self.__sweep else time.sleep(1)
                if not self.__record:
                    if len(df) > 0:
                        df.loc[1] = ["Timestamp (Relative)"] + list(
                            map(
                                lambda x: datetime.datetime.fromtimestamp(
                                    timestamp=df.columns[1:].max() - x,
                                    tz=datetime.timezone.utc,
                                ).strftime("%H:%M:%S:%f"),
                                df.columns[1:],
                            )
                        )

                        spectrogram.writer(
                            properties=[],
                            frequencies=[],
                            spectrogram=df,
                            filename=self.__output_file,
                        )

                    df = {}
                    total = 0
                    continue

                arr = []
                while not slices_queue.empty():
                    arr.append(slices_queue.get())

                if len(arr) > 0:
                    if len(df) == 0:
                        data = {}
                        data["Timestamp"] = [
                            "Timestamp (Absolute)",
                            "Timestamp (Relative)",
                            "Frequency [Hz]",
                        ] + list(list(map(lambda x: x.slice.keys(), arr))[0])
                        df = pd.DataFrame(data)

                    for el in arr:
                        df[el.timestamp] = [
                            el.datetime,
                            el.timestamp,
                            "Magnitude [dBm]",
                        ] + list(el.slice.values())

                    total += len(arr)
                    url = f"http://localhost:{self.__conf["global"]["port"]}/viewer/add"
                    api = req(url=url, method="post", json_body=jsonpickle.encode(arr))
                    if api and api[0] == 200:
                        if api[1]["code"] == "OK":
                            print(
                                f"{datetime.datetime.now()}: {len(arr)}/{total}. API: ✅"
                            )
                        else:
                            print(
                                f"{datetime.datetime.now()}: {len(arr)}/{total}. API: 🚸"
                            )
                    else:
                        print(f"{datetime.datetime.now()}: {len(arr)}/{total}. API: ❌")

        self.__thread_api_get = threading.Thread(target=background_api_client)
        self.__thread_api_get.daemon = True
        self.__thread_api_get.start()

        if "instrument" in self.__conf:
            self.__connect_instr(instr=self.__conf["instrument"])
        else:
            self.__connect_instr(instr=None)

        basic_view.show()
