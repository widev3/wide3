import pandas as pd
import io
import numpy as np
import time
import datetime
import re


class Spectrogram(object):
    def __init__(self):
        pass

    def __split_file_by_empty_lines(self):
        with open(self.__filename, "r") as file:
            lines = file.readlines()
            chunks = []
            current_chunk = []

            for line in lines:
                if line.strip() == "":
                    if current_chunk:
                        chunks.append(current_chunk)
                        current_chunk = []
                else:
                    current_chunk.append(line)

            if current_chunk:
                chunks.append(current_chunk)

        return chunks

    def __properties(self, file):
        return pd.read_csv(io.StringIO("".join(file)), sep=self.__separator)

    def __frequencies(self, file):
        return pd.read_csv(io.StringIO("".join(file)), sep=self.__separator)

    def __spectrogram(self, file):
        def qty_and_unit(string):
            match = re.match(r"(.+)\s\[(.+)\]", string)
            if match:
                quantity = match.group(1).strip()  # Group 1 is the quantity
                unit = match.group(2).strip()  # Group 2 is the unit of measure
                return quantity, unit
            return None, None

        def milliseconds(strptime):
            return int(
                (
                    strptime.microsecond
                    + 1000000
                    * (strptime.second + strptime.minute * 60 + strptime.hour * 3600)
                )
                / 1000
            )

        if len(file) < 3:
            return None

        # absolute timestamp
        absolute_tss = []
        try:
            absolute_tss = list(
                map(
                    lambda x: time.mktime(
                        datetime.datetime.strptime(x, "%H:%M:%S %d/%m/%Y").timetuple()
                    ),
                    pd.read_csv(
                        io.StringIO(file[0]), sep=self.__separator, header=None
                    ).values[0][1:-1],
                )
            )
        except:
            try:
                absolute_tss = list(
                    map(
                        lambda x: time.mktime(
                            datetime.datetime.strptime(
                                x, "%H:%M:%S %m/%d/%Y"
                            ).timetuple()
                        ),
                        pd.read_csv(
                            io.StringIO(file[0]), sep=self.__separator, header=None
                        ).values[0][1:-1],
                    )
                )
            except:
                return None

        # relative time interval with respect to start)
        try:
            relative_tss_zero_end = list(
                map(
                    lambda x: milliseconds(
                        datetime.datetime.strptime(x, "%H:%M:%S:%f")
                    ),
                    pd.read_csv(
                        io.StringIO(file[1]), sep=self.__separator, header=None
                    ).values[0][1:-1],
                )
            )
        except:
            return None

        relative_tss_zero_start = list(
            map(lambda x: relative_tss_zero_end[0] - x, relative_tss_zero_end)
        )

        spec = pd.read_csv(io.StringIO("\n".join(file[2:])), sep=self.__separator)
        columns = spec.columns
        for column in columns:
            spec = spec.drop(column, axis=1) if np.isnan(spec[column]).all() else spec
        spec = spec.rename(
            columns=dict(
                map(
                    lambda x: (spec.columns[x[0] + 1], x[1]),
                    enumerate(relative_tss_zero_start),
                )
            )
        )

        frequency = spec[spec.columns[0]]  # frequencies
        magnitude = np.array(list(map(lambda x: x[1:], spec.values)))  # magnitudes
        um = {}
        um["time"] = "ms"
        um["frequency"] = qty_and_unit(frequency.name)[1]
        um["magnitude"] = tuple(
            list(set(map(lambda x: qty_and_unit(x), columns[1:-1])))[0]
        )

        return {
            "r": relative_tss_zero_start,
            "a": absolute_tss,
            "f": list(map(lambda x: x + self.__lo, frequency)),
            "m": magnitude,
            "u": um,
        }

    def read_file(self, filename: str, separator: str, lo: float):
        self.__filename = filename
        self.__separator = separator
        self.__lo = lo

        chunks = self.__split_file_by_empty_lines()
        self.prop = self.__properties(chunks[0])
        self.freq = self.__frequencies(chunks[1])
        self.spec = self.__spectrogram(chunks[2])

    def write_file(self, filename: str):
        self.prop.to_csv(filename, index=False, header=False)
        with open(filename, "a") as f:
            f.write("\n")

        self.freq.to_csv(filename, mode="a", index=False)
        with open(filename, "a") as f:
            f.write("\n")

        df = pd.DataFrame()

        row = [
            ["Timestamp (Relative)"]
            + list(
                map(
                    lambda x: datetime.datetime.strftime(
                        datetime.datetime.fromtimestamp(x),
                        "%H:%M:%S %m/%d/%Y",
                    ),
                    self.spec["r"],
                )
            )
        ]
        df = pd.concat([df, pd.DataFrame(row)])

        row = [["Frequency [Hz]"] + ["Magnitude [dBm]"] * len(self.spec["m"][0])]
        df = pd.concat([df, pd.DataFrame(row)])

        df = pd.concat(
            [
                df,
                pd.DataFrame(
                    map(
                        lambda x: [x[1]] + list(self.spec["m"][x[0]]),
                        enumerate(self.spec["f"]),
                    )
                ),
            ]
        )

        df.columns = ["Timestamp (Absolute)"] + list(
            map(
                lambda x: datetime.datetime.strftime(
                    datetime.datetime.fromtimestamp(x), "%H:%M:%S %m/%d/%Y"
                ),
                self.spec["a"],
            )
        )
        df.to_csv(filename, mode="a", index=False)

    def time_slice(self, x):
        return self.spec["m"][x]

    def freq_slice(self, x):
        return self.spec["m"][:, x]
