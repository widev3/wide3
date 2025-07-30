from single_include import (
    datetime,
    time,
    timezone,
    SkyCoord,
    AltAz,
    EarthLocation,
    Time,
    units,
)


class Dashboard:

    def test(self):

        # 1. Define observer's location (e.g., Mauna Kea Observatory)
        location = EarthLocation(
            lat=19.8207 * units.deg, lon=-155.4681 * units.deg, height=4205 * units.m
        )

        # 2. Define observation time (UTC)
        while True:
            time.sleep(1)
            obstime = Time(datetime.now(timezone.utc))

            # 3. Define target coordinates in ICRS (J2000) frame
            ra = 10.684 * units.deg  # Example: RA of Andromeda Galaxy
            dec = 41.269 * units.deg  # Dec of Andromeda Galaxy
            j2000_coord = SkyCoord(ra=ra, dec=dec, frame="icrs")

            # 4. Define the AltAz frame
            altaz_frame = AltAz(obstime=obstime, location=location)

            # 5. Transform to AltAz
            altaz_coord = j2000_coord.transform_to(altaz_frame)

            # 6. Print the result
            print(f"Altitude: {altaz_coord.alt}, Azimuth: {altaz_coord.az}")

    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        self.test()
