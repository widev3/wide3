import random
import matplotlib.colors as mcolors
import astropy.units as u
import traceback
from BasicView import BasicView, plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.widgets import Button, CheckButtons
from Config import Config
from astroquery.vizier import Vizier
from astropy.coordinates import SkyCoord, EarthLocation
from mount_control.lib.CoordinateConverter import CoordinateConverter


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
        self.__scatter_markers = ".,ovo^<>1234sp*H+hxDd|_"

    def __is_light_color(self, color, threshold=0.8):
        rgb = mcolors.to_rgb(color)
        return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2] > threshold

    def __get_sky_map_coordinates(self, catalog_name):
        vizier = Vizier(columns=["*", "+_r"], row_limit=-1)
        catalog_list = vizier.find_catalogs(catalog_name)
        if len(catalog_list) == 1 and list(catalog_list.keys())[0] == None:
            BasicView.basic_view_show_message(
                "Mount control", f"No catalog called {catalog_name}", 2
            )
            return [], []

        catalogs = vizier.get_catalogs(list(catalog_list.keys()))
        catalog, index = BasicView.basic_view_checkbox_list(
            "Mount control",
            "Select a catalog",
            list(
                map(lambda x: f"{x} ({str(len(catalogs[x]))} records)", catalogs.keys())
            ),
            True,
        )

        catalog = catalogs[index]
        ra_field, index = BasicView.basic_view_checkbox_list(
            "Mount control", "Select RA field", catalog.columns.keys(), True
        )
        dec_field, index = BasicView.basic_view_checkbox_list(
            "Mount control", "Select DEC field", catalog.columns.keys(), True
        )

        coords = list(
            map(
                lambda x: SkyCoord(
                    ra=x[ra_field],
                    dec=x[dec_field],
                    unit=(u.deg, u.deg),
                    frame="icrs",
                ),
                catalog,
            )
        )

        magnitude = []

        return coords, magnitude

    def __setup_sky_map(self, event=None, clear_all=False):
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
            try:
                coords, magnitude = self.__get_sky_map_coordinates(catalog_name)
                coordinate_converter = CoordinateConverter(
                    EarthLocation(lat=45 * u.deg, lon=10 * u.deg, height=20 * u.m),
                    coords,
                )
                coords = coordinate_converter.eq_to_altaz()
                self.__im["sky_map"][catalog_name] = self.__ax["sky_map"].scatter(
                    [coord.az.deg for coord in coords],
                    [coord.alt.deg for coord in coords],
                    marker=random.choice(self.__scatter_markers),
                    color=random.choice(self.__scatter_colors),
                    s=20,
                )

                self.__ax["sky_map"].xaxis.set_minor_locator(AutoMinorLocator(1))
                self.__ax["sky_map"].yaxis.set_minor_locator(AutoMinorLocator(1))
                self.__ax["sky_map"].grid(**BasicView.grid_arguments())
                self.__ax["sky_map"].set_title(f"{catalog_name} catalog")
                # self.__ax["sky_map"].set_xlim([min(az), max(az)])
                # self.__ax["sky_map"].set_ylim([min(alt), max(alt)])

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
            except:
                BasicView.basic_view_show_message(
                    "Mount control",
                    f"Error during the loading of catalog\n{traceback.format_exc()}",
                    3,
                )

    def __hide_show_catalog(self, label):
        self.__im["sky_map"][label].set_visible(
            not self.__im["sky_map"][label]._visible
        )
        plt.draw()

    def __on_full_sky_button_clicked(self, event):
        self.__ax["sky_map"].set_xlim([-10, 370])
        self.__ax["sky_map"].set_ylim([-100, 100])
        plt.draw()

    def view(self):
        mosaic = [
            ["sky_map", "load_catalog"],
            ["sky_map", "clear_and_load_catalog"],
            ["sky_map", "clear"],
            ["sky_map", "full_sky"],
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
            lambda x: self.__setup_sky_map(event=x, clear_all=False)
        )

        clear_and_load_catalog_button = Button(
            self.__ax["clear_and_load_catalog"], "Clear and load catalog"
        )
        clear_and_load_catalog_button.on_clicked(
            lambda x: self.__setup_sky_map(event=x, clear_all=True)
        )

        clear_button = Button(self.__ax["clear"], "Clear")
        clear_button.on_clicked(lambda x: self.__setup_sky_map(clear_all=True))

        full_sky_button = Button(self.__ax["full_sky"], "Full sky")
        full_sky_button.on_clicked(lambda x: self.__on_full_sky_button_clicked(x))

        self.__setup_sky_map(self.__config.data["catalog_name"])

        plt.show(block=True)
