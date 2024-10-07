import numpy as np
import astropy.units as u
import random
import traceback
from BasicView import BasicView, plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.widgets import Button, CheckButtons
from Config import Config
from astroquery.vizier import Vizier
from astropy.coordinates import EarthLocation
from mount_control.lib.CoordinateConverter import CatalogCoordinate
from matplotlib.animation import FuncAnimation
from astropy.coordinates import SkyCoord
from matplotlib.lines import Line2D


class View(object):
    def __init__(self):
        self.__config = Config("mount_control")
        self.ax = {}
        self.im = {}
        self.loaded_catalogs = {}
        self.__scatter_markers = ".,ov^<>12348sp*hH+xdD|_"
        self.__scatter_colors = [
            "darkslategray",
            "lightcoral",
            "peachpuff",
            "deepskyblue",
            "chartreuse",
            "orangered",
            "plum",
            "navajowhite",
            "khaki",
            "mediumseagreen",
            "thistle",
            "powderblue",
            "lightgreen",
            "gold",
            "mistyrose",
            "slateblue",
            "mediumvioletred",
            "violet",
            "dodgerblue",
            "springgreen",
            "lightsalmon",
            "wheat",
            "tomato",
            "red",
        ]

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

        return self.coordinate_converter.extract_coordinate(
            catalog, ra_field, dec_field
        )

    def __setup_observers(self):
        self.observers_position = [
            SkyCoord(
                az=0 * u.deg,
                alt=90 * u.deg,
                location=self.coordinate_converter.location,
                obstime=self.coordinate_converter.now(),
                frame="altaz",
            ),
            SkyCoord(
                az=12.5 * u.deg,
                alt=60 * u.deg,
                location=self.coordinate_converter.location,
                obstime=self.coordinate_converter.now(),
                frame="altaz",
            ),
        ]
        coords = list(
            map(
                lambda x: self.coordinate_converter.altaz_to_eq(x),
                self.observers_position,
            )
        )
        self.im["sky_map"] = self.ax["sky_map"].scatter(
            [coord.ra.deg for coord in coords],
            [coord.dec.deg for coord in coords],
            color="black",
            marker="X",
            s=100,
        )

        def __update_observers(self, frame):
            offsets = self.im["sky_map"].get_offsets()
            for index in range(len(self.observers_position)):
                offsets[index] = (
                    offsets[index][0] + random.uniform(-1, 1),
                    offsets[index][1] + random.uniform(-1, 1),
                )

            self.im["sky_map"].set_offsets(offsets)

            return (self.im["sky_map"],)

        if not hasattr(self, "animations"):
            self.animations = FuncAnimation(
                self.__fig,
                lambda x: __update_observers(self, x),
                interval=100,
                blit=True,
                cache_frame_data=False,
            )

    def __setup_sky_map(self, event=None, clear_all=False):
        if isinstance(event, str):
            catalog_name = event
        elif event:
            catalog_name = BasicView.basic_view_text_input(
                "Mount control", "Catalog name"
            )

        if clear_all:
            self.ax["sky_map"].cla()

        if catalog_name and catalog_name not in self.loaded_catalogs:
            try:
                self.loaded_catalogs[catalog_name] = self.__get_sky_map_coordinates(
                    catalog_name
                )

                ra = [coord.ra.deg for coord in self.loaded_catalogs[catalog_name]]
                dec = [coord.dec.deg for coord in self.loaded_catalogs[catalog_name]]
                self.im["sky_map"] = self.ax["sky_map"].scatter(
                    ra,
                    dec,
                    color=self.__scatter_colors[len(self.loaded_catalogs) - 1],
                    marker=self.__scatter_markers[len(self.loaded_catalogs) - 1],
                    s=20,
                )

                self.ax["sky_map"].set_xlim([min(ra), max(ra)])
                self.ax["sky_map"].set_ylim([min(dec), max(dec)])
                self.ax["sky_map"].legend(
                    handles=list(
                        map(
                            lambda x: Line2D(
                                [0],
                                [0],
                                marker=self.__scatter_markers[x[0]],
                                color="w",
                                label=x[1],
                                markerfacecolor=self.__scatter_colors[x[0]],
                                markersize=10,
                            ),
                            enumerate(self.loaded_catalogs),
                        )
                    ),
                    loc="upper center",
                    bbox_to_anchor=(0.5, -0.05),
                    fancybox=True,
                    ncol=4,
                )

                self.__setup_observers()

                plt.show()
            except:
                BasicView.basic_view_show_message(
                    "Mount control",
                    f"Error during the loading of catalog\n{traceback.format_exc()}",
                    3,
                )

    def __on_full_sky_button_clicked(self, event):
        self.ax["sky_map"].set_xlim([-10, 370])
        self.ax["sky_map"].set_ylim([-100, 100])
        plt.draw()

    def view(self):
        mosaic = [
            ["sky_map", "load_catalog"],
            ["sky_map", "clear_and_load_catalog"],
            ["sky_map", "clear"],
            ["sky_map", "full_sky"],
            ["sky_map", None],
        ]
        self.__fig, self.ax = BasicView.basic_view(
            "Mount control",
            mosaic=mosaic,
            width_ratios=[8, 1],
            height_ratios=[1, 1, 1, 1, 20],
        )

        load_catalog_button = Button(self.ax["load_catalog"], "Load catalog")
        load_catalog_button.on_clicked(
            lambda x: self.__setup_sky_map(event=x, clear_all=False)
        )

        clear_and_load_catalog_button = Button(
            self.ax["clear_and_load_catalog"], "Clear and load catalog"
        )
        clear_and_load_catalog_button.on_clicked(
            lambda x: self.__setup_sky_map(event=x, clear_all=True)
        )

        clear_button = Button(self.ax["clear"], "Clear")
        clear_button.on_clicked(lambda x: self.__setup_sky_map(clear_all=True))

        full_sky_button = Button(self.ax["full_sky"], "Full sky")
        full_sky_button.on_clicked(lambda x: self.__on_full_sky_button_clicked(x))

        self.coordinate_converter = CatalogCoordinate(
            EarthLocation(lat=45 * u.deg, lon=10 * u.deg, height=20 * u.m)
        )

        self.ax["sky_map"].set_xlabel("RA")
        self.ax["sky_map"].set_ylabel("DEC")
        self.ax["sky_map"].xaxis.set_minor_locator(AutoMinorLocator(1))
        self.ax["sky_map"].yaxis.set_minor_locator(AutoMinorLocator(1))
        self.ax["sky_map"].grid(**BasicView.grid_arguments())
        self.ax["sky_map"].set_title("Sky map")

        self.__setup_observers()
        self.__setup_sky_map(self.__config.data["catalog_name"])

        plt.show(block=True)
