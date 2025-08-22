from astropy.time import Time
from datetime import datetime
from datetime import timezone

def now_utc():
    return Time(datetime.now(timezone.utc))