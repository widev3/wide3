import random
import matplotlib.colors as mcolors
import astropy.units as u
from BasicView import BasicView, plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.widgets import Button, CheckButtons
from Config import Config
from astropy.coordinates import SkyCoord
from astroquery.vizier import Vizier


class View(object):
    def __init__(self):
        self.__config = Config("mount_control")
        self.__ax = {}
        self.__im = {}
        self.__scatter_colors = [
            name
            for name, color in mcolors.CSS4_COLORS.items()
            if not self.__is_light_color(color)
        ]
        self.__scatter_markers = [
            ".",
            ",",
            "o",
            "v",
            "^",
            "<",
            ">",
            "1",
            "2",
            "3",
            "4",
            "s",
            "p",
            "*",
            "h",
            "H",
            "+",
            "x",
            "D",
            "d",
            "|",
            "_",
        ]

    def __is_light_color(self, color, threshold=0.8):
        rgb = mcolors.to_rgb(color)
        return (
            0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2] > threshold
        )  # 0.299*R + 0.587*G + 0.114*B (ITU-R BT.601)

    def __update_sky_map(self, catalog_name):
        vizier = Vizier(columns=["*", "+_r"], row_limit=-1)
        catalog_list = vizier.find_catalogs(catalog_name)
        if len(catalog_list) == 1 and list(catalog_list.keys())[0] == None:
            BasicView.basic_view_show_message(
                "Mount control", f"No catalog called {catalog_name}", 2
            )
            return [], []

        catalogs = vizier.get_catalogs(list(catalog_list.keys()))
        catalog = catalogs[0]

        BasicView.basic_view_checkbox_list("Mount control", "Select coordinated", catalog.columns.keys())

        coords = list(
            map(
                lambda x: SkyCoord(
                    ra=x["RAJ2000"],
                    dec=x["DEJ2000"],
                    unit=(u.deg, u.deg),
                    frame="icrs",
                ),
                catalog,
            )
        )

        ra = list(map(lambda x: x.ra.deg, coords))
        dec = list(map(lambda x: x.dec.deg, coords))

        return ra, dec

    def __refresh_sky_map(self, event=None, clear_all=False):
        if isinstance(event, str):
            catalog_name = event
        elif event:
            catalog_name = BasicView.basic_view_text_input(
                "Mount control", "Catalog name"
            )

        if "sky_map" not in self.__im:
            self.__im["sky_map"] = {}

        if clear_all:
            self.__im["sky_map"] = {}
            self.__ax["sky_map"].cla()

        if catalog_name not in self.__im["sky_map"]:
            ra, dec = self.__update_sky_map(catalog_name)
            if ra and dec:
                self.__im["sky_map"][catalog_name] = self.__ax["sky_map"].scatter(
                    ra,
                    dec,
                    marker=random.choice(self.__scatter_markers),
                    color=random.choice(self.__scatter_colors),
                    s=20,
                )

                self.__ax["sky_map"].xaxis.set_minor_locator(AutoMinorLocator(1))
                self.__ax["sky_map"].yaxis.set_minor_locator(AutoMinorLocator(1))
                self.__ax["sky_map"].grid(**BasicView.grid_arguments())
                self.__ax["sky_map"].set_title(f"{catalog_name} catalog")
                self.__ax["sky_map"].set_xlim([min(ra), max(ra)])
                self.__ax["sky_map"].set_ylim([min(dec), max(dec)])

                if hasattr(self, "__catalogs_check"):
                    self.__catalogs_check.ax.clear()

                inset = self.__ax["sky_map"].inset_axes([0.0, 0.0, 0.12, 0.2])
                self.__catalogs_check = CheckButtons(
                    ax=inset,
                    labels=list(self.__im["sky_map"]),
                    actives=list(
                        map(lambda x: x._visible, self.__im["sky_map"].values())
                    ),
                    frame_props={"s": [64] * len(self.__im["sky_map"])},
                )
                self.__catalogs_check.on_clicked(self.__hide_show_catalog)

                plt.show()

    def __hide_show_catalog(self, label):
        self.__im["sky_map"][label].set_visible(
            not self.__im["sky_map"][label]._visible
        )
        plt.draw()

    def view(self):
        mosaic = [
            ["sky_map", "load_catalog"],
            ["sky_map", "clear_and_load_catalog"],
            ["sky_map", "clear"],
            ["sky_map", "save_catalogs_as_default"],
            ["sky_map", None],
        ]
        self.__fig, self.__ax = BasicView.basic_view(
            "Mount control",
            mosaic=mosaic,
            width_ratios=[8, 1],
            height_ratios=[1, 1, 1, 1, 20],
        )

        load_catalog_button = Button(self.__ax["load_catalog"], "Load catalog")
        load_catalog_button.on_clicked(
            lambda x: self.__refresh_sky_map(event=x, clear_all=False)
        )

        clear_and_load_catalog_button = Button(
            self.__ax["clear_and_load_catalog"], "Clear and load catalog"
        )
        clear_and_load_catalog_button.on_clicked(
            lambda x: self.__refresh_sky_map(event=x, clear_all=True)
        )

        clear_button = Button(self.__ax["clear"], "Clear")
        clear_button.on_clicked(lambda x: self.__refresh_sky_map(clear_all=True))

        save_as_default_catalogs_button = Button(
            self.__ax["save_catalogs_as_default"], "Save catalogs as default"
        )
        # save_as_default_catalogs_button.on_clicked(
        #     lambda: self.__refresh_sky_map(clear_all=True)
        # )

        # inset = self.__ax["sky_map"].inset_axes([0.0, 0.0, 0.12, 0.2])
        # self.__catalogs_check = CheckButtons(ax=inset, labels=[], actives=[])
        self.__refresh_sky_map(self.__config.data["catalog_name"])

        plt.show(block=True)
