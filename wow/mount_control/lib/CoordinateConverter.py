import astropy.units as u
from astropy.time import Time
from astropy.coordinates import AltAz, SkyCoord
from datetime import datetime, timezone


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

    def eq_to_altaz(self, coords, time=None):
        if not time:
            time = Time(datetime.now(tz=timezone.utc), scale="utc")
        altaz_converter = AltAz(location=self.location, obstime=time)
        return list(map(lambda x: x.transform_to(altaz_converter), coords))
