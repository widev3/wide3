import pandas as pd
import io
import numpy as np
import time
import datetime
import re


def __milliseconds(strptime):
    return int(
        (
            strptime.microsecond
            + 1000000 * (strptime.second + strptime.minute * 60 + strptime.hour * 3600)
        )
        / 1000
    )


def extract_quantity_and_unit(string):
    match = re.match(r"(.+)\s\[(.+)\]", string)
    if match:
        quantity = match.group(1).strip()  # Group 1 is the quantity
        unit = match.group(2).strip()  # Group 2 is the unit of measure
        return quantity, unit
    return None, None


def spectrogram(file, config):
    # absolute timestamp
    absolute_tss = []
    try:
        absolute_tss = list(
            map(
                lambda x: time.mktime(
                    datetime.datetime.strptime(x, "%H:%M:%S %d/%m/%Y").timetuple()
                ),
                pd.read_csv(
                    io.StringIO(file[0]), sep=config.data["separator"], header=None
                ).values[0][1:-1],
            )
        )
    except:
        absolute_tss = list(
            map(
                lambda x: time.mktime(
                    datetime.datetime.strptime(x, "%H:%M:%S %m/%d/%Y").timetuple()
                ),
                pd.read_csv(
                    io.StringIO(file[0]), sep=config.data["separator"], header=None
                ).values[0][1:-1],
            )
        )

    # relative time interval with respect to start)
    relative_tss_zero_end = list(
        map(
            lambda x: __milliseconds(datetime.datetime.strptime(x, "%H:%M:%S:%f")),
            pd.read_csv(
                io.StringIO(file[1]), sep=config.data["separator"], header=None
            ).values[0][1:-1],
        )
    )

    relative_tss_zero_start = list(
        map(lambda x: relative_tss_zero_end[0] - x, relative_tss_zero_end)
    )

    spec = pd.read_csv(io.StringIO("\n".join(file[2:])), sep=config.data["separator"])
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
    um["frequency"] = extract_quantity_and_unit(frequency.name)[1]
    um["magnitude"] = tuple(
        list(set(map(lambda x: extract_quantity_and_unit(x), columns[1:-1])))[0]
    )

    return {
        "relative_time": relative_tss_zero_start,
        "absolute_time": absolute_tss,
        "frequency": frequency,
        "magnitude": magnitude,
        "um": um,
    }
