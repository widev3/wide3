import matplotlib.pyplot as plt
import astropy.units as u
from matplotlib.widgets import Button, CheckButtons
from basic_view import plt
from Config import Config
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


def view():
    config = Config("mount_control")

    # check = CheckButtons(
    #     ax=rax,
    #     labels=lines_by_label.keys(),
    #     actives=[l.get_visible() for l in lines_by_label.values()],
    #     label_props={"color": line_colors},
    #     frame_props={"edgecolor": line_colors},
    #     check_props={"facecolor": line_colors},
    # )

    # def callback(label):
    #     ln = lines_by_label[label]
    #     ln.set_visible(not ln.get_visible())
    #     ln.figure.canvas.draw_idle()

    # check.on_clicked(callback)

    def refresh_sky_map(event):
        if isinstance(event, str):
            catalog_name = event
        else:
            catalog_name = basic_view_text_input("Mount control", "Catalog name")
        ra, dec = __update_sky_map(catalog_name)

        if "sky_map" in im:
            im["sky_map"].remove()

        im["sky_map"] = ax["sky_map"].scatter(ra, dec, marker="o", color="blue", s=20)
        ax["sky_map"].grid(True)
        ax["sky_map"].set_title(f"{catalog_name} catalog")
        ax["sky_map"].set_xlim([min(ra) * 0.80, max(ra) * 1.20])
        ax["sky_map"].set_ylim([min(dec) * 0.80, max(dec) * 1.20])
        plt.show()

    mosaic = [["sky_map", "catalogs"], ["sky_map", "options"]]
    fig, ax = basic_view(
        "Mount control", mosaic=mosaic, width_ratios=[10, 1], height_ratios=[1, 20]
    )

    im = {}
    refresh_sky_map(config.data["catalog_name"])

    text_box = Button(ax["catalogs"], "Load catalog")
    text_box.on_clicked(lambda x: refresh_sky_map(x))

    plt.show(block=True)
