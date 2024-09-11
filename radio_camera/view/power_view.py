import math
import numpy as np
from view.basic_view import basic_view, plt


def power_view(event, spectrogram):
    fig = basic_view("Power")
    mosaic = [["t_power"], ["f_power"]]
    ax = fig.subplot_mosaic(
        mosaic=mosaic,
        empty_sentinel=None,
        height_ratios=[5, 5],
    )

    power_spectrogram = [
        [math.pow(10, (el - 30) / 10) for el in row] for row in spectrogram["i"]
    ]

    t_power_spectrogram = [
        sum(row[i] for row in power_spectrogram)
        for i in range(len(power_spectrogram[0]))
    ]
    ax["t_power"].set_title("Time power")
    ax["t_power"].set_xlabel("Relative time from start [ms]")
    ax["t_power"].set_ylabel("Power [dBmW]")
    t_power_x = np.linspace(
        min(spectrogram["t"]),
        max(spectrogram["t"]),
        num=len(t_power_spectrogram),
    )
    ax["t_power"].plot(t_power_x, t_power_spectrogram)
    # ax["t_power"].set_xlim(xlim)

    f_power_spectrogram = [math.log(sum(el)) for el in power_spectrogram]
    ax["f_power"].set_title("Frequency power")
    ax["f_power"].set_xlabel("Frequency [MHz]")
    ax["f_power"].set_ylabel("Power [dBmW]")
    f_power_x = np.linspace(
        min(spectrogram["f"] / 1000000),
        max(spectrogram["f"] / 1000000),
        num=len(f_power_spectrogram),
    )
    ax["f_power"].plot(f_power_x, f_power_spectrogram)
    # ax["f_power"].set_xlim(3000)

    plt.show()
