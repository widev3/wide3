import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.widgets import RadioButtons, Slider
from view.Cursor import Cursor
from view.Lims import Lims
from view.basic_view import basic_view


def __gamma_slider_changed(val, im, vmin, vmax, fig):
    im.set_norm(cm.colors.PowerNorm(gamma=val, vmin=vmin, vmax=vmax))
    fig.canvas.draw_idle()


def main_view(config, properties, frequencies, spectrogram):

    fig = basic_view("Radio camera")

    mosaic = [
        ["spectrogram", "colorbar", "f_proj", "t_power"],
        ["spectrogram", "colorbar", "f_proj", "f_power"],
        ["gamma_setting_slider", "band_selection", "band_selection", "f_power"],
        ["t_proj", "band_selection", "band_selection", "f_power"],
    ]
    ax = fig.subplot_mosaic(
        mosaic=mosaic,
        empty_sentinel=None,
        width_ratios=[15, 1, 3, 15],
        height_ratios=[5, 1, 0.1, 2],
    )

    im = {}
    vmax = np.max(spectrogram["i"])
    vmin = np.min(spectrogram["i"])
    im["spectrogram"] = ax["spectrogram"].imshow(
        X=spectrogram["i"],
        norm=cm.colors.PowerNorm(gamma=config.data["gamma"], vmin=vmin, vmax=vmax),
        cmap=config.data["cmap"],
        aspect="auto",
        origin="lower",
        extent=[
            min(spectrogram["t"]),
            max(spectrogram["t"]),
            min(spectrogram["f"] / 1000000),
            max(spectrogram["f"] / 1000000),
        ],
    )

    lims = Lims(im)
    ax["spectrogram"].callbacks.connect("xlim_changed", lims.on_xlim_changed)
    ax["spectrogram"].callbacks.connect("ylim_changed", lims.on_ylim_changed)
    ax["spectrogram"].set_title("Spectrogram")
    ax["spectrogram"].set_xlabel("Relative time from start [ms]")
    ax["spectrogram"].set_ylabel("Frequency [MHz]")
    ax["spectrogram"].grid(True, linestyle="--", color="gray", alpha=0.7)
    fig.colorbar(im["spectrogram"], cax=ax["colorbar"])

    (im["t_proj"],) = ax["t_proj"].plot([], [])
    ax["t_proj"].set_title("Time projection")
    ax["t_proj"].set_xlabel("Relative time from start [ms]")
    ax["t_proj"].set_ylabel("Power [dBmW]")
    ax["t_proj"].set_xlim(im["spectrogram"].get_extent()[0:2])
    ax["t_proj"].margins(x=0)
    ax["t_proj"].grid(True, linestyle="--", color="gray", alpha=0.7)

    (im["f_proj"],) = ax["f_proj"].plot([], [])
    ax["f_proj"].set_title("Frequency projection")
    ax["f_proj"].set_xlabel("Frequency [MHz]")
    ax["f_proj"].set_ylabel("Power [dBmW]")
    ax["f_proj"].set_ylim(im["spectrogram"].get_extent()[2:4])
    ax["f_proj"].margins(y=0)
    ax["f_proj"].is_rotated = True
    ax["f_proj"].grid(True, linestyle="--", color="gray", alpha=0.7)

    gamma_slider = Slider(
        ax=ax["gamma_setting_slider"],
        label="Gamma",
        valmin=0,
        valmax=1,
        valinit=im["spectrogram"].norm.gamma,
    )
    gamma_slider.on_changed(
        (
            lambda event: __gamma_slider_changed(
                event, im["spectrogram"], vmin, vmax, fig
            )
        )
    )

    ax["band_selection"].set_title("Band [MHz-MHz]")
    band_selection_radiobuttons = RadioButtons(
        ax=ax["band_selection"],
        radio_props={"s": list(map(lambda x: 64, config.data["bands"]))},
        labels=list(
            map(lambda x: f"{x} {config.data['bands'][x]}", config.data["bands"].keys())
        ),
    )

    power_spectrogram = [
        [math.pow(10, (el - 30) / 10) for el in row] for row in spectrogram["i"]
    ]

    t_power_spectrogram = [
        sum(row[i] for row in power_spectrogram) * 1000
        for i in range(len(power_spectrogram[0]))
    ]
    (im["t_power"],) = ax["t_power"].plot(
        np.linspace(
            min(spectrogram["t"]),
            max(spectrogram["t"]),
            num=len(t_power_spectrogram),
        ),
        t_power_spectrogram,
    )
    ax["t_power"].set_title("Time power")
    ax["t_power"].set_xlabel("Relative time from start [ms]")
    ax["t_power"].set_ylabel("Power [µW]")
    ax["t_power"].grid(True, linestyle="--", color="gray", alpha=0.7)

    f_power_spectrogram = [math.log10(sum(el) * 1000) for el in power_spectrogram]
    (im["f_power"],) = ax["f_power"].plot(
        np.linspace(
            min(spectrogram["f"] / 1000000),
            max(spectrogram["f"] / 1000000),
            num=len(f_power_spectrogram),
        ),
        f_power_spectrogram,
    )
    ax["f_power"].set_title("Frequency power")
    ax["f_power"].set_xlabel("Frequency [MHz]")
    ax["f_power"].set_ylabel("Power [log10(µW)]")
    ax["f_power"].grid(True, linestyle="--", color="gray", alpha=0.7)

    cursor = Cursor(ax, im)
    plt.connect("button_press_event", cursor.button_press_event)

    plt.show(block=True)
