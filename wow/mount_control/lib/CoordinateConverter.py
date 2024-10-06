import astropy.units as u
from astropy.time import Time
from astropy.coordinates import AltAz
from datetime import datetime, timezone


class CoordinateConverter:
    def __init__(self, location, coords):
        self.location = location
        self.coords = coords

    def eq_to_altaz(self, time=Time(datetime.now(tz=timezone.utc), scale="utc")):
        altaz_converter = AltAz(location=self.location, obstime=time)
        return list(map(lambda x: x.transform_to(altaz_converter), self.coords))
