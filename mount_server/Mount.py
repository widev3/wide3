import time
from astropy import units
from datetime import datetime
from datetime import timezone
from astropy.time import Time
from astropy.coordinates import AltAz
from astropy.coordinates import SkyCoord
from astropy.coordinates import EarthLocation


class Mount:
    def __init__(self, location: EarthLocation):
        self.__moving = False
        self.__location = location
        self.__target = None
        self.__offset = None
        self.__behavior = "follow"

    def set_altaz_target(self, alt, az):
        self.__target = SkyCoord(
            alt=alt,
            az=az,
            frame=AltAz(
                obstime=Time(datetime.now(timezone.utc)), location=self.__location
            ),
        )

    def set_radec_target(self, ra, dec):
        self.__target = SkyCoord(ra=ra, dec=dec, frame="icrs").transform_to(
            AltAz(obstime=Time(datetime.now(timezone.utc)), location=self.__location)
        )

    def set_ra_offset(self, ra):
        radec = SkyCoord(
            alt=self.__target.alt,
            az=self.__target.az,
            frame=AltAz(
                obstime=Time(datetime.now(timezone.utc)),
                location=self.__location,
            ),
        ).transform_to("icrs")

        radec = SkyCoord(ra=radec.ra - ra * units.deg, dec=radec.dec, frame="icrs")

        self.__offset = radec.transform_to(
            AltAz(
                obstime=Time(datetime.now(timezone.utc)),
                location=self.__location,
            )
        )

    def set_dec_offset(self, dec):
        radec = SkyCoord(
            alt=self.__target.alt,
            az=self.__target.az,
            frame=AltAz(
                obstime=Time(datetime.now(timezone.utc)),
                location=self.__location,
            ),
        ).transform_to("icrs")

        radec = SkyCoord(ra=radec.ra, dec=radec.dec - dec * units.deg, frame="icrs")

        self.__offset = radec.transform_to(
            AltAz(
                obstime=Time(datetime.now(timezone.utc)),
                location=self.__location,
            )
        )

    def set_alt_offset(self, alt):
        self.__offset = SkyCoord(
            alt=self.__target.alt - alt * units.deg,
            az=self.__target.az,
            frame=AltAz(
                obstime=Time(datetime.now(timezone.utc)),
                location=self.__location,
            ),
        )

    def set_az_offset(self, az):
        self.__offset = SkyCoord(
            alt=self.__target.alt,
            az=self.__target.az - az * units.deg,
            frame=AltAz(
                obstime=Time(datetime.now(timezone.utc)),
                location=self.__location,
            ),
        )

    def set_behavior(self, behavior: str):
        self.__behavior = behavior

    def is_moving(self):
        return self.__moving

    def move(self):
        self.__moving = True
        if self.__offset:
            print(
                f"{self.__behavior} offset position {self.__offset.alt}, {self.__offset.az}"
            )
        elif self.__target:
            print(
                f"{self.__behavior} target position {self.__target.alt}, {self.__target.az}"
            )
        else:
            print("No movement")

        time.sleep(1)
        self.__moving = False
