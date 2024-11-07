import astropy.units as u
import random
import traceback
import utils
import Viewer
from BasicView import BasicView, FuncAnimation, Line2D, Button
from astropy.coordinates import EarthLocation
from mount_control.lib.CoordinateConverter import CatalogCoordinate
from astropy.coordinates import SkyCoord


class View(object):
    def __init__(self, conf):
        if not conf:
            conf = {}
            conf["package"] = __package__
            conf["name"] = utils.package_to_name(__package__)
            conf["catalog_name"] = ""

        self.__config = conf
        self.__ax = {}
        self.__im = {}
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
        vizier = astroquery.vizier.Vizier(columns=["*", "+_r"], row_limit=-1)
        catalog_list = vizier.find_catalogs(catalog_name)
        if len(catalog_list) == 1 and list(catalog_list.keys())[0] == None:
            BasicView.basic_view_show_message(
                self.__config["name"], f"No catalog called {catalog_name}", 2
            )
            return [], []

        catalogs = vizier.get_catalogs(list(catalog_list.keys()))
        catalog, index = BasicView.basic_view_checkbox_list(
            self.__config["name"],
            "Select a catalog",
            list(
                map(lambda x: f"{x} ({str(len(catalogs[x]))} records)", catalogs.keys())
            ),
            True,
        )

        catalog = catalogs[index]
        ra_field, index = BasicView.basic_view_checkbox_list(
            self.__config["name"], "Select RA field", catalog.columns.keys(), True
        )
        dec_field, index = BasicView.basic_view_checkbox_list(
            self.__config["name"], "Select DEC field", catalog.columns.keys(), True
        )

        return self.__coordinate_converter.extract_coordinate(
            catalog, ra_field, dec_field
        )

    def __setup_observers(self):
        self.observers_position = [
            SkyCoord(
                az=0 * u.deg,
                alt=90 * u.deg,
                location=self.__coordinate_converter.location,
                obstime=self.__coordinate_converter.now(),
                frame="altaz",
            ),
            SkyCoord(
                az=12.5 * u.deg,
                alt=60 * u.deg,
                location=self.__coordinate_converter.location,
                obstime=self.__coordinate_converter.now(),
                frame="altaz",
            ),
        ]
        coords = list(
            map(
                lambda x: self.__coordinate_converter.altaz_to_eq(x),
                self.observers_position,
            )
        )
        self.__im["sky_map"] = self.__ax["sky_map"].scatter(
            [coord.ra.deg for coord in coords],
            [coord.dec.deg for coord in coords],
            color="black",
            marker="X",
            s=100,
        )

        def __update_observers(self, frame):
            offsets = self.__im["sky_map"].get_offsets()
            for index in range(len(self.observers_position)):
                offsets[index] = (
                    offsets[index][0] + random.uniform(-1, 1),
                    offsets[index][1] + random.uniform(-1, 1),
                )

            self.__im["sky_map"].set_offsets(offsets)

            return (self.__im["sky_map"],)

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
                self.__config["name"], "Catalog name"
            )

        if clear_all:
            self.__ax["sky_map"].cla()

        if catalog_name and catalog_name not in self.loaded_catalogs:
            try:
                self.loaded_catalogs[catalog_name] = self.__get_sky_map_coordinates(
                    catalog_name
                )

                ra = [coord.ra.deg for coord in self.loaded_catalogs[catalog_name]]
                dec = [coord.dec.deg for coord in self.loaded_catalogs[catalog_name]]
                self.__im["sky_map"] = self.__ax["sky_map"].scatter(
                    ra,
                    dec,
                    color=self.__scatter_colors[len(self.loaded_catalogs) - 1],
                    marker=self.__scatter_markers[len(self.loaded_catalogs) - 1],
                    s=20,
                )

                self.__ax["sky_map"].set_xlim([min(ra), max(ra)])
                self.__ax["sky_map"].set_ylim([min(dec), max(dec)])
                self.__ax["sky_map"].legend(
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
            except:
                BasicView.basic_view_show_message(
                    self.__config["name"],
                    f"Error during the loading of catalog\n{traceback.format_exc()}",
                    3,
                )
        else:
            self.__on_full_sky_button_clicked(None)

    def __on_full_sky_button_clicked(self, event):
        self.__ax["sky_map"].set_xlim([-10, 370])
        self.__ax["sky_map"].set_ylim([-100, 100])
        BasicView.refresh()

    def view(self):
        mosaic = BasicView.generate_array(50, 50)
        buttons = [
            "radio_camera",
            "mount_control",
            None,
            None,
            None,
            None,
            "-",
            "load",
            "clear_and_load",
            "clear",
            "full_sky",
        ]
        BasicView.fill_row_with_array(mosaic, (1, 1), (50, 2), buttons)

        BasicView.fill_with_string(mosaic, (1, 2), (50, 50), "sky_map", (1, 2))

        self.__fig, self.__ax = BasicView.basic_view(self.__config["name"], mosaic)

        BasicView.buttons_frame(self, self.__ax, self.__config["package"])

        self.__ax["-"].axvline(x=0.5, color="black", linestyle="-", linewidth=5)
        self.__ax["-"].axis("off")

        self.__load_button = Button(self.__ax["load"], "Load")
        self.__load_button.on_clicked(
            lambda x: self.__setup_sky_map(event=x, clear_all=False)
        )

        self.__clear_and_load_button = Button(
            self.__ax["clear_and_load"], "Clear & load"
        )
        self.__clear_and_load_button.on_clicked(
            lambda x: self.__setup_sky_map(event=x, clear_all=True)
        )

        self.__clear_button = Button(self.__ax["clear"], "Clear")
        self.__clear_button.on_clicked(lambda x: self.__setup_sky_map(clear_all=True))

        self.__full_sky_button = Button(self.__ax["full_sky"], "Full sky")
        self.__full_sky_button.on_clicked(
            lambda x: self.__on_full_sky_button_clicked(x)
        )

        self.__coordinate_converter = CatalogCoordinate(
            EarthLocation(lat=45 * u.deg, lon=10 * u.deg, height=20 * u.m)
        )

        self.__ax["sky_map"].set_xlabel("RA")
        self.__ax["sky_map"].set_ylabel("DEC")
        self.__ax["sky_map"].set_title("Sky map")
        BasicView.set_grid(self.__ax["sky_map"])

        self.__setup_observers()
        self.__setup_sky_map(self.__config["catalog_name"])

        BasicView.show()
