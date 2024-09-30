import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import astropy.units as u
from basic_view import plt
from mount_control.lib.Config import Config
from astropy.coordinates import SkyCoord
from astroquery.vizier import Vizier
from basic_view import basic_view, basic_view_text_input


def __update_sky_map(catalog_name):
    vizier = Vizier(columns=["*", "+_r"], row_limit=-1)
    catalog_list = vizier.find_catalogs(catalog_name)
    catalogs = vizier.get_catalogs(list(catalog_list.keys()))
    ngc_catalog = catalogs[0]

    coords = list(
        map(
            lambda x: SkyCoord(
                ra=x["RAJ2000"],
                dec=x["DEJ2000"],
                unit=(u.deg, u.deg),
                frame="icrs",
            ),
            ngc_catalog,
        )
    )

    ra = list(map(lambda x: x.ra.deg, coords))
    dec = list(map(lambda x: x.dec.deg, coords))

    return ra, dec


def view(config):
    config = Config(config)
    catalog_name = "I/151"
    ra, dec = __update_sky_map(catalog_name)

    mosaic = [["catalogs", "options"], ["sky_map", "options"]]
    fig, ax = basic_view(
        "Mount control", mosaic=mosaic, width_ratios=[10, 1], height_ratios=[1, 50]
    )

    im = {}
    im["sky_map"] = ax["sky_map"].scatter(
        ra, dec, marker="o", color="red", s=20, label="Messier objects"
    )

    ax["sky_map"].grid(True)
    ax["sky_map"].set_xlabel("Right Ascension")
    ax["sky_map"].set_ylabel("Declination")
    ax["sky_map"].set_title(f"{catalog_name} catalog")

    def refresh_sky_map(event):
        catalog_name = basic_view_text_input()
        ra, dec = __update_sky_map(catalog_name)
        ax["sky_map"].clear()
        im["sky_map"] = ax["sky_map"].scatter(
            ra, dec, marker="o", color="red", s=20, label="Messier objects"
        )
        plt.show()

    text_box = Button(ax["catalogs"], "Display catalog")
    text_box.on_clicked(lambda x: refresh_sky_map(x))

    plt.show(block=True)
