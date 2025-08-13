import time

from utils import now_utc
from astropy.coordinates import AltAz
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation


class Mount:
    def __init__(self):
        self.__moving = False
        self.__location = None
        self.__target = None  # it is always in alt/az
        self.__offset = None  # it is always in alt/az
        self.__behavior = None

    def set_location(self, location: EarthLocation):
        self.__location = location

    def set_target(self, alt=None, az=None, ra=None, dec=None):
        if alt is not None and az is not None:
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            self.__target = SkyCoord(alt=alt, az=az, frame=altaz_frame)
        elif ra is not None and dec is not None:
            sky_coord = SkyCoord(ra=ra, dec=dec, frame="icrs")
            altaz_frame = AltAz(obstime=now_utc(), location=self.__location)
            self.__target = sky_coord.transform_to(altaz_frame)

    def set_absolute_offset(self, alt=None, az=None, ra=None, dec=None):
        self.__offset = SkyCoord(
            alt=self.__target.alt,
            az=self.__target.az,
            frame=AltAz(obstime=now_utc(), location=self.__location),
        )
        # if alt is not None and az is not None:
        #     self.__offset = SkyCoord(
        #         alt=alt,
        #         az=az,
        #         frame=AltAz(
        #             obstime=Time(datetime.now()), location=self.__location
        #         ),
        #     )

        # if ra is not None and dec is not None:
        #     self.__offset = SkyCoord(ra=ra, dec=dec, frame="icrs").transform_to(
        #         AltAz(
        #             obstime=Time(datetime.now()), location=self.__location
        #         )
        #     )

    def set_relative_offset(self, alt=None, az=None, ra=None, dec=None):
        self.__offset = SkyCoord(
            alt=self.__target.alt,
            az=self.__target.az,
            frame=AltAz(obstime=now_utc(), location=self.__location),
        )

    # def set_absolute_offset(self, alt=None, az=None, ra=None, dec=None):
    #     if alt is not None:
    #         self.__offset = SkyCoord(
    #             alt=self.__target.alt - alt * units.deg,
    #             az=self.__target.az,
    #             frame=AltAz(
    #                 obstime=Time(datetime.now()), location=self.__location
    #             ),
    #         )

    #     if az is not None:
    #         self.__offset = SkyCoord(
    #             alt=self.__target.alt,
    #             az=self.__target.az - az * units.deg,
    #             frame=AltAz(
    #                 obstime=Time(datetime.now()), location=self.__location
    #             ),
    #         )

    #     if ra is not None:
    #         radec = SkyCoord(
    #             alt=self.__target.alt,
    #             az=self.__target.az,
    #             frame=AltAz(
    #                 obstime=Time(datetime.now()), location=self.__location
    #             ),
    #         ).transform_to("icrs")

    #         radec = SkyCoord(ra=radec.ra - ra * units.deg, dec=radec.dec, frame="icrs")

    #         self.__offset = radec.transform_to(
    #             AltAz(
    #                 obstime=Time(datetime.now()), location=self.__location
    #             )
    #         )

    #     if dec is not None:
    #         radec = SkyCoord(
    #             alt=self.__target.alt,
    #             az=self.__target.az,
    #             frame=AltAz(
    #                 obstime=Time(datetime.now()), location=self.__location
    #             ),
    #         ).transform_to("icrs")

    #         radec = SkyCoord(ra=radec.ra, dec=radec.dec - dec * units.deg, frame="icrs")

    #         self.__offset = radec.transform_to(
    #             AltAz(
    #                 obstime=Time(datetime.now()), location=self.__location
    #             )
    #         )

    def set_behavior(self, behavior: str):
        self.__behavior = behavior

    def is_moving(self):
        return self.__moving

    def has_location(self):
        return self.__location is not None

    def run(self):
        self.__moving = True
        if self.__offset:
            print(f"{self.__behavior} offset {self.__offset.alt}, {self.__offset.az}")
        elif self.__target:
            print(f"{self.__behavior} target {self.__target.alt}, {self.__target.az}")
        else:
            print("No movement")

        time.sleep(1)
        self.__moving = False
