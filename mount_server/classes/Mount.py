import drivers.mount
from utils import now_utc
from astropy import units
from astropy.coordinates import AltAz
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation


class Mount:
    def __init__(self):
        self.__moving = False
        self.__location = None
        self.__target = None  # it is always in alt/az
        self.__offset = None  # it is always in alt/az

    def get_moving(self):
        return self.__moving

    def get_location(self):
        return self.__location

    def get_target(self):
        return self.__target

    def get_offset(self):
        return self.__offset

    def set_location(self, location: EarthLocation):
        self.__location = location

    def set_target(
        self, alt: float = None, az: float = None, ra: float = None, dec: float = None
    ) -> None:
        if alt and az:
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            self.__target = SkyCoord(alt=alt, az=az, frame=altaz_frame)
        elif ra and dec:
            sky_coord = SkyCoord(ra=ra, dec=dec, frame="icrs")
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            self.__target = sky_coord.transform_to(altaz_frame)

    def set_absolute_offset(
        self, alt: float = None, az: float = None, ra: float = None, dec: float = None
    ) -> None:
        if alt or az:
            self.__offset = SkyCoord(
                alt=alt * units.deg if alt else self.__target.alt,
                az=az * units.deg if az else self.__target.az,
                frame=AltAz(obstime=now_utc(), location=self.__location),
            )
        elif ra or dec:
            altaz_coord = SkyCoord(
                alt=self.__target.alt,
                az=self.__target.az,
                obstime=now_utc(),
                frame="altaz",
                location=self.__location,
            )
            icrs_coord = altaz_coord.transform_to("icrs")
            sky_coord = SkyCoord(
                ra=ra * units.deg if ra else icrs_coord.ra,
                dec=dec * units.deg if dec else icrs_coord.dec,
                frame="icrs",
            )
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            self.__offset = sky_coord.transform_to(altaz_frame)

    def set_relative_offset(
        self, alt: float = None, az: float = None, ra: float = None, dec: float = None
    ) -> None:
        if alt or az:
            self.__offset = SkyCoord(
                alt=self.__target.alt - alt * units.deg if alt else self.__target.alt,
                az=self.__target.az - az * units.deg if az else self.__target.az,
                frame=AltAz(obstime=now_utc(), location=self.__location),
            )
        elif ra or dec:
            altaz_coord = SkyCoord(
                alt=self.__target.alt,
                az=self.__target.az,
                obstime=now_utc(),
                frame="altaz",
                location=self.__location,
            )
            icrs_coord = altaz_coord.transform_to("icrs")
            sky_coord = SkyCoord(
                ra=icrs_coord.ra - ra * units.deg if ra else icrs_coord.ra,
                dec=icrs_coord.dec - dec * units.deg if dec else icrs_coord.dec,
                frame="icrs",
            )
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            self.__offset = sky_coord.transform_to(altaz_frame)

    def run(self, bh: str) -> None:
        print(f"{bh} ", end="")
        if bh == "follow":
            print(f"{self.__target.alt}, {self.__target.az}")
        elif bh == "transit":
            print(
                f"{self.__target.alt}, {self.__target.az} from {self.__offset.alt}, {self.__offset.az}"
            )
        elif bh == "route":
            print(
                f"{self.__target.alt}, {self.__target.az} from {self.__offset.alt}, {self.__offset.az}"
            )

        self.__moving = True
        drivers.mount.run(self.__target.az, self.__target.alt)
        self.__moving = False
