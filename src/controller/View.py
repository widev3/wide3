import sys
import jsonpickle
import time
import queue
import random
import requests
import threading
import numpy as np
import pandas as pd
import basic_view
import traceback
from utils import check_server
from datetime import datetime
from RsInstrument import RsInstrument


class View(object):
    def __init__(self, conf):
        self.__conf = conf
        self.__ax = {}
        self.__record = False
        self.__instr = None

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
            self.__instr.write("INIT:CONT ON")

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

            self.__instr_write()

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
        self.__record = False
        self.__ax["record"].cla()
        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Start record"
        )
        self.__record_button.on_clicked(self.__start_record)

    def __start_record(self, x):
        self.__record = True
        self.__ax["record"].cla()
        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Stop record"
        )
        self.__record_button.on_clicked(self.__stop_record)

        self.__instr.write("INIT:CONT OFF") if self.__instr else None

    def __instr_write(self, x=None):
        self.__freq = float(self.__central_text_box.text) * 10**6
        self.__span = float(self.__span_text_box.text) * 10**6
        self.__sweep = float(self.__sweep_text_box.text) * 10**-3
        self.__instr.write(f"SENS:FREQ:CENT {self.__freq}") if self.__instr else None
        self.__instr.write(f"SENS:FREQ:SPAN {self.__span}") if self.__instr else None
        self.__instr.write(f"SENS:SWE:TIME {self.__sweep}") if self.__instr else None

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
        self.__connect_sa_button.on_clicked(lambda x: self.__connect_instr(instr=None))

        self.__record_button = basic_view.Button(
            ax=self.__ax["record"], label="Start record"
        )
        # self.__record_button.on_clicked(lambda x: None)
        self.__record_button.on_clicked(self.__start_record)
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

        spectrogram_queue = queue.Queue()

        def background_instr():

            class Slice:
                def __init__(self, datetime, timestamp, slice):
                    self.datetime = datetime
                    self.timestamp = timestamp
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
                if not self.__record:
                    time.sleep(0.1)
                else:
                    time.sleep(self.__sweep)
                    self.__instr.write("INIT:IMM") if self.__instr else None
                    self.__instr.query_opc() if self.__instr else None

                    data = (
                        self.__instr.query_str("TRACE:DATA?") if self.__instr else None
                    )
                    values = [random.uniform(0, 1) for _ in range(1000)]
                    # values = [float(value) for value in data.split(",")]
                    slice = time_slice(values, cent=self.__freq, span=self.__span)
                    spectrogram_queue.put(
                        Slice(
                            datetime=datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
                            timestamp=time.time(),
                            slice=slice,
                        )
                    )

        self.__thread_instr = threading.Thread(target=background_instr)
        self.__thread_instr.daemon = True
        self.__thread_instr.start()

        def background_api_client():
            url = f"http://localhost:{self.__conf["global"]["port"]}/viewer/setup"
            send_by_api = check_server(url=url)
            output_file = f"{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"
            if send_by_api:
                response = requests.get(url)

            df = {}
            while True:
                time.sleep(0.1)
                if not self.__record and len(df) > 0:
                    df.loc[1] = ["Timestamp (Relative)"] + list(
                        map(
                            lambda x: str(
                                pd.to_datetime(df.columns[1:].max() - x).time()
                            ).replace(".", ":"),
                            df.columns[1:],
                        )
                    )
                    df.to_csv(output_file, index=False, sep=",")
                    df = {}
                elif not spectrogram_queue.empty():
                    print(f"{datetime.now()}: sent {spectrogram_queue.qsize()} slices")

                    if send_by_api:
                        url = f"http://localhost:{self.__conf["global"]["port"]}/viewer/add"
                        response = requests.post(url, json=jsonpickle.encode(arr))
                        if response.status_code == 200:
                            print("Response JSON:", response.json())
                        else:
                            print("Error:", response.status_code, response.text)
                    else:
                        if len(df) == 0:
                            data = {}
                            data["Timestamp"] = [
                                "Timestamp (Absolute)",
                                "Timestamp (Relative)",
                                "Frequency [Hz]",
                            ] + list(spectrogram_queue.get().slice.keys())
                            df = pd.DataFrame(data)

                        while not spectrogram_queue.empty():
                            s = spectrogram_queue.get()
                            df[s.timestamp] = [
                                s.datetime,
                                0,
                                "Magnitude [dBm]",
                            ] + list(s.slice.values())

        self.__thread_api_get = threading.Thread(target=background_api_client)
        self.__thread_api_get.daemon = True
        self.__thread_api_get.start()

        self.__connect_instr(
            instr=self.__conf["instrument"] if "instrument" in self.__conf else None
        )

        basic_view.show()
