import numpy as np
from view.basic_view import basic_view, plt
from matplotlib import cm


def fft_view(event, config, spectrogram):
    fft = np.log10(abs(np.fft.fft2(spectrogram["i"])))
    fig = basic_view("FFT")
    mosaic = [["fft"]]
    ax = fig.subplot_mosaic(mosaic=mosaic, empty_sentinel=None)

    vmax = max(max(sublist) for sublist in fft)
    vmin = min(min(sublist) for sublist in fft)
    im = ax["fft"].imshow(
        X=fft,
        norm=cm.colors.PowerNorm(gamma=config.data["gamma"], vmin=vmin, vmax=vmax),
        cmap=config.data["cmap"],
        aspect="auto",
        origin="lower",
        # extent=[
        #     min(spectrogram["t"]),
        #     max(spectrogram["t"]),
        #     min(spectrogram["f"] / 1000000),
        #     max(spectrogram["f"] / 1000000),
        # ],
    )

    plt.show()
