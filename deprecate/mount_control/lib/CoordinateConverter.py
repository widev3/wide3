import astropy.units as u
from astropy.time import Time
from astropy.coordinates import AltAz, SkyCoord
from datetime import datetime, timezone
from astropy.utils.iers.iers import conf


class CatalogCoordinate:
    def __init__(self, location):
        self.location = location

    def extract_coordinate(self, catalog, ra_field, dec_field):
        return list(
            map(
                lambda x: SkyCoord(
                    ra=x[ra_field], dec=x[dec_field], unit=(u.deg, u.deg), frame="icrs"
                ),
                catalog,
            )
        )

    def now(self):
        return Time(datetime.now(tz=timezone.utc), scale="utc")

    def eq_to_altaz(self, coord, time=None):
        if not time:
            time = Time(datetime.now(tz=timezone.utc), scale="utc")

        frame = AltAz(location=self.location, obstime=time)
        return coord.transform_to(frame)

    def altaz_to_eq(self, coord, time=None):
        if not time:
            time = Time(datetime.now(tz=timezone.utc), scale="utc")

        coord = SkyCoord(
            alt=coord.alt,
            az=coord.az,
            obstime=time,
            frame="altaz",
            location=self.location,
        )
        return coord.icrs
