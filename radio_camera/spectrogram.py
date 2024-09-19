import pandas as pd
import io
import numpy as np
import time
import datetime
import re


def milliseconds(strptime):
    return int(
        (
            strptime.microsecond
            + 1000000 * (strptime.second + strptime.minute * 60 + strptime.hour * 3600)
        )
        / 1000
    )


def spectrogram(file):
    absolute_tss = list(
        map(
            lambda x: time.mktime(
                datetime.datetime.strptime(x, "%H:%M:%S %m/%d/%Y").timetuple()
            ),
            pd.read_csv(io.StringIO(file[0]), sep=",", header=None).values[0][1:-1],
        )
    )
    relative_tss_zero_end = list(
        map(
            lambda x: milliseconds(datetime.datetime.strptime(x, "%H:%M:%S:%f")),
            pd.read_csv(io.StringIO(file[1]), sep=",", header=None).values[0][1:-1],
        )
    )
    relative_tss_zero_start = list(
        map(lambda x: relative_tss_zero_end[0] - x, relative_tss_zero_end)
    )
    spec = pd.read_csv(io.StringIO("\n".join(file[2:])), sep=",")
    columns = spec.columns
    for column in columns:
        spec = spec.drop(column, axis=1) if np.isnan(spec[column]).all() else spec
    ums = list(map(lambda x: re.findall(r"\[(.*?)\]", x)[0], spec.columns))
    spec = spec.rename(
        columns=dict(
            map(
                lambda x: (spec.columns[x[0] + 1], x[1]),
                enumerate(relative_tss_zero_start),
            )
        )
    )

    t = relative_tss_zero_start  # times
    f = spec[spec.columns[0]]  # frequencies
    i = np.array(list(map(lambda x: x[1:], spec.values)))  # intensities

    return {"t": t, "f": f, "i": i}
