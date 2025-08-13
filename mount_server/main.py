import sys

sys.dont_write_bytecode = True

import uuid
from routes.mount import mount_bp
from flask import Flask, request, jsonify

app = Flask(__name__)

app.register_blueprint(mount_bp, url_prefix="/mount")

global session_name
session_name = None


@app.before_request
def middleware():
    global session_name
    token = request.headers.get("Authorization")
    if token and session_name and token != str(session_name):
        return jsonify({"error": "Unauthorized"}), 401
    if token and not session_name:
        return jsonify({"error": "Unauthorized"}), 401
    if not token and request.path != "/session/acquire":
        return jsonify({"error": "Unauthorized"}), 401


@app.route("/session/acquire", methods=["GET"])
def session_acquire():
    global session_name
    if not session_name:
        session_name = uuid.uuid4()
        return jsonify({"session_name": session_name}), 200

    return jsonify({"message": "session in use"}), 403


@app.route("/session/release", methods=["GET"])
def session_release():
    global session_name
    if session_name:
        session_name = None
        return jsonify({"message": "OK"}), 200

    return jsonify({"message": "cannot release an empty session"}), 403


if __name__ == "__main__":
    app.run(debug=True)

# from astropy.coordinates import SkyCoord, EarthLocation, AltAz
# from astropy.time import Time
# import astropy.units as u
# from datetime import datetime
# import pytz  # To handle timezones

# # Example: RA/Dec of the star (ICRS, J2000)
# ra = "18h55m"
# ra = 18.916666667 * u.deg
# dec = "-26d17m"
# dec = -26.283333333 * u.deg
# star = SkyCoord(ra=ra, dec=dec, frame="icrs")

# # Observer's location (example: New York City)
# location = EarthLocation(lat=45.3833 * u.deg, lon=10.668056 * u.deg, height=145 * u.m)

# # Local datetime with timezone
# # local_tz = pytz.timezone("America/Rome")
# dt_local = datetime.now()

# # Convert to Astropy Time (UTC)
# time = Time(dt_local.astimezone(pytz.UTC))

# # AltAz frame for the given time and location
# altaz_frame = AltAz(obstime=time, location=location)
# altaz = star.transform_to(altaz_frame)

# print(f"Altitude: {altaz.alt:.2f}")
# print(f"Azimuth: {altaz.az:.2f}")
