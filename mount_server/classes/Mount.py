from time import sleep
import numpy as np
import drivers.mount
from utils import now_utc
from astropy.coordinates import AltAz
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation
from astropy import units


class Mount:
    def __init__(self):
        self.__moving = False
        self.__location = None
        self.__target = None  # it is always in icrs
        self.__offset = None  # it is always in icrsù
        self.__running = False

    def __linear_path(self, start: SkyCoord, end: SkyCoord) -> SkyCoord:
        ra_vals = np.arange(start.ra.deg, end.ra.deg, 0.2)
        dec_vals = np.arange(start.dec.deg, end.dec.deg, 0.2)
        ints = int((len(ra_vals) ** 2 + len(dec_vals) ** 2) ** 0.5 + 1)
        ra_vals = np.linspace(start.ra.deg, end.ra.deg, ints) * units.deg
        dec_vals = np.linspace(start.dec.deg, end.dec.deg, ints) * units.deg
        return SkyCoord(ra=ra_vals, dec=dec_vals, frame=start.frame)

    def get_running(self):
        return self.__running

    def get_location(self):
        return self.__location

    def get_target(self):
        return self.__target

    def get_offset(self):
        return self.__offset

    def set_location(self, location: EarthLocation):
        self.__location = location

    def set_target(self, alt=None, az=None, ra=None, dec=None) -> None:
        if alt is not None and az is not None:
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            altaz_coords = SkyCoord(alt=alt, az=az, frame=altaz_frame)
            self.__target = altaz_coords.transform_to("icrs")
        elif ra is not None and dec is not None:
            self.__target = SkyCoord(ra=ra, dec=dec, frame="icrs")

    def set_absolute_offset(self, alt=None, az=None, ra=None, dec=None) -> None:
        if alt is not None or az is not None:
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            altaz_coords = self.__target.transform_to(altaz_frame)
            altaz_coords = SkyCoord(
                alt=alt if alt is not None else altaz_coords.alt,
                az=az if az is not None else altaz_coords.az,
                frame=altaz_frame,
            )
            self.__offset = altaz_coords.transform_to("icrs")
        elif ra is not None or dec is not None:
            self.__offset = SkyCoord(
                ra=ra if ra is not None else self.__target.ra,
                dec=dec if dec is not None else self.__target.dec,
                frame="icrs",
            )

    def set_relative_offset(self, alt=None, az=None, ra=None, dec=None) -> None:
        if alt is not None or az is not None:
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            altaz_coords = self.__target.transform_to(altaz_frame)
            altaz_coords = SkyCoord(
                alt=altaz_coords.alt - alt if alt is not None else altaz_coords.alt,
                az=altaz_coords.az - az if az is not None else altaz_coords.az,
                frame=altaz_frame,
            )
            self.__offset = altaz_coords.transform_to("icrs")
        elif ra is not None or dec is not None:
            self.__offset = SkyCoord(
                ra=self.__target.ra - ra if ra is not None else self.__target.ra,
                dec=self.__target.dec - dec if dec is not None else self.__target.dec,
                frame="icrs",
            )

    def run(self, bh: str) -> None:
        print(f"behaviour {bh}")
        if self.__target is not None:
            print(f"target {self.__target.ra}, {self.__target.dec}")
        if self.__offset is not None:
            print(f"offset {self.__offset.ra}, {self.__offset.dec}")

        self.__running = True
        if bh == "follow":
            while self.__running:
                altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
                altaz_coords = self.__target.transform_to(altaz_frame)
                print(f"{altaz_coords.az}, {altaz_coords.alt}")
                # drivers.mount.run(self.__target.az, self.__target.alt)
                sleep(1)
        elif bh == "transit":
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            altaz_coords = self.__target.transform_to(altaz_frame)
            print(f"{altaz_coords.az}, {altaz_coords.alt}")
            # drivers.mount.run(self.__target.az, self.__target.alt)
        elif bh == "route":
            path_coords = self.__linear_path(start=self.__offset, end=self.__target)
            for path_coord in path_coords:
                altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
                altaz_coords = path_coord.transform_to(altaz_frame)
                print(f"{altaz_coords.az}, {altaz_coords.alt}")
                # drivers.mount.run(self.__target.az, self.__target.alt)
                sleep(5)

        print("Done run")

    def stop(self) -> None:
        self.__running = False
