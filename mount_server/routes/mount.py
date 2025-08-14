import math
import threading
from pathlib import Path
from astropy import units
from classes.Mount import Mount
from flask import request, jsonify, Blueprint
from astropy.coordinates import EarthLocation

mount_bp = Blueprint(Path(__file__).stem, __name__)

global mount
mount = Mount()


def is_float(value: str) -> bool:
    try:
        f = float(value)
        return math.isfinite(f)
    except:
        return False


@mount_bp.route("/location", methods=["POST"])
def mount_location():
    global mount
    if mount.get_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty body"}), 400

    if "lat" not in data:
        return jsonify({"error": "Missing required field: lat"}), 400

    lat = data["lat"]
    lat = lat * units.deg if is_float(lat) else lat

    if "lon" not in data:
        return jsonify({"error": "Missing required field: lon"}), 400

    lon = data["lon"]
    lon = lon * units.deg if is_float(lon) else lon

    if "height" not in data:
        return jsonify({"error": "Missing required field: height"}), 400

    height = data["height"]
    height = height * units.m if is_float(height) else height
    mount.set_location(EarthLocation(lat=lat, lon=lon, height=height))

    return jsonify({"message": "OK"}), 200


@mount_bp.route("/target", methods=["POST"])
def mount_target():
    global mount
    if mount.get_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty body"}), 400

    if "ra" in data and "dec" not in data:
        return jsonify({"error": "Missing required field: target.dec"}), 400

    if "dec" in data and "ra" not in data:
        return jsonify({"error": "Missing required field: target.ra"}), 400

    if "alt" in data and "az" not in data:
        return jsonify({"error": "Missing required field: target.az"}), 400

    if "az" in data and "alt" not in data:
        return jsonify({"error": "Missing required field: target.alt"}), 400

    if "ra" in data and "alt" in data:
        return jsonify({"error": "Target should be in ra/dec or alt/az"}), 400

    if "az" in data:
        alt = data["alt"]
        az = data["az"]
        alt = alt * units.deg if is_float(alt) else alt
        az = az * units.deg if is_float(az) else az
        mount.set_target(alt=alt, az=az)
        return (
            jsonify(
                {
                    "message": "OK",
                    "target": {
                        "alt": mount.get_target().alt.deg,
                        "az": mount.get_target().az.deg,
                    },
                }
            ),
            200,
        )
    elif "ra" in data:
        ra = data["ra"]
        dec = data["dec"]
        ra = ra * units.deg if is_float(ra) else ra
        dec = dec * units.deg if is_float(dec) else dec
        mount.set_target(ra=ra, dec=dec)
        return (
            jsonify(
                {
                    "message": "OK",
                    "target": {
                        "alt": mount.get_target().alt.deg,
                        "az": mount.get_target().az.deg,
                    },
                }
            ),
            200,
        )
    else:
        return jsonify({"error": "Neither ra/dec nor alt/az"}), 400


@mount_bp.route("/offset", methods=["POST"])
def mount_offset():
    global mount
    if mount.get_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty body"}), 400

    if "absolute" in data:
        absolute = data["absolute"]
        if "ra" in absolute and (ra := absolute["ra"]):
            mount.set_absolute_offset(ra=ra)
        if "dec" in absolute and (dec := absolute["dec"]):
            mount.set_absolute_offset(dec=dec)
        if "alt" in absolute and (alt := absolute["alt"]):
            mount.set_absolute_offset(alt=alt)
        if "az" in absolute and (az := absolute["az"]):
            mount.set_absolute_offset(az=az)
    elif "relative" in data:
        relative = data["relative"]
        if "ra" in relative and (ra := relative["ra"]):
            mount.set_relative_offset(ra=ra)
        if "dec" in relative and (dec := relative["dec"]):
            mount.set_relative_offset(dec=dec)
        if "alt" in relative and (alt := relative["alt"]):
            mount.set_relative_offset(alt=alt)
        if "az" in relative and (az := relative["az"]):
            mount.set_relative_offset(az=az)
    elif "timedelta" in data:
        timedelta = data["timedelta"]
        dec_g = int(15 * timedelta / 3600)
        timedelta -= 3600 * dec_g / 15
        dec_m = int(timedelta / 60)
        timedelta -= dec_m * 60
        dec_s = timedelta
        dec = dec_g + dec_m / 60 + dec_s / 3600
        mount.set_relative_offset(dec=dec)
    else:
        return jsonify({"error": "Neither absolute nor relative nor timedelta"}), 400

    return (
        jsonify(
            {
                "message": "OK",
                "offset": {
                    "alt": mount.get_offset().alt.deg,
                    "az": mount.get_offset().az.deg,
                },
            }
        ),
        200,
    )


@mount_bp.route("/run", methods=["GET"])
def mount_run():
    global mount
    if mount.get_location() is None:
        return jsonify({"error": "Mount location is not set"}), 400

    if not mount.get_target():
        return jsonify({"error": "Mount target is not set"}), 400

    bh = request.args.get("bh")
    if bh == "follow":
        return jsonify({"message": "OK"}), 200
    elif bh == "transit":
        if not mount.get_offset():
            return jsonify({"error": "Mount offset is not set"}), 400
    elif bh == "route":
        if not mount.get_offset():
            return jsonify({"error": "Mount offset is not set"}), 400
    else:
        return jsonify({"error": "bh is not 'follow', 'transit' or 'route'"}), 400

    thread = threading.Thread(target=lambda: mount.run(bh))
    thread.start()

    return jsonify({"message": "OK"}), 200
