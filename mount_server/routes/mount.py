import math
import threading
from Mount import Mount
from pathlib import Path
from astropy import units
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
    if mount.is_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty body"}), 400

    if "lat" not in data:
        return jsonify({"error": "Missing required field: lat"}), 400

    lat = data["lat"]
    if not is_float(lat):
        return jsonify({"error": "Invalid value. lat must be a number"}), 400

    if "lon" not in data:
        return jsonify({"error": "Missing required field: lon"}), 400

    lon = data["lon"]
    if not is_float(lon):
        return jsonify({"error": "Invalid value. lon must be a number"}), 400

    if "height" not in data:
        return jsonify({"error": "Missing required field: height"}), 400

    height = data["height"]
    if not is_float(height):
        return jsonify({"error": "Invalid value. height must be a number"}), 400

    lat *= units.deg
    lon *= units.deg
    height *= units.m
    mount.set_location(EarthLocation(lat=lat, lon=lon, height=height))

    return jsonify({"message": "OK"}), 200


@mount_bp.route("/target", methods=["POST"])
def mount_target():
    global mount
    if mount.is_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()

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
        if not is_float(alt) or not is_float(az):
            return jsonify({"error": "Invalid value. alt and az must be numbers"}), 400

        alt *= units.deg
        az *= units.deg
        mount.set_target(alt=alt, az=az)
    elif "ra" in data:
        ra = data["ra"]
        dec = data["dec"]
        if not is_float(ra) or not is_float(dec):
            return jsonify({"error": "Invalid value. ra and dec must be numbers"}), 400

        ra *= units.deg
        dec *= units.deg
        mount.set_target(ra=ra, dec=dec)
    else:
        return jsonify({"error": "Neither ra/dec nor alt/az"}), 400

    return jsonify({"message": "OK"}), 200


@mount_bp.route("/offset", methods=["POST"])
def mount_offset():
    global mount
    if mount.is_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()

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
        dec = 123  # compute from timedelta
        mount.set_relative_offset(dec=dec)
    else:
        return (jsonify({"error": "Neither absolute nor relative nor timedelta"}), 400)

    return jsonify({"message": "OK"}), 200

    # if "ra" in data and (ra := data["ra"]) is not None:
    #     ra = data["ra"]
    #     mount.set_absolute_offset(ra=ra)

    #     if "dec" in data:
    #         dec = data["dec"]
    #         mount.set_absolute_offset(dec=dec)
    # elif ("az" in data or "alt" in data) and not ("ra" in data or "dec" in data):
    #     if "az" in data:
    #         az = data["az"]
    #         mount.set_absolute_offset(az=az)

    #     if "alt" in data:
    #         alt = data["alt"]
    #         mount.set_absolute_offset(alt=alt)
    # else:
    #     return jsonify({"error": "Cannot set offset"}), 400

    # if "behavior" in data:
    #     behavior = data["behavior"]
    #     if behavior not in ["follow", "transit", "towards"]:
    #         return jsonify({"error": f"Invalid behavior {behavior}"}), 400

    #     mount.set_behavior(behavior)

    # thread = threading.Thread(target=mount.goto)
    # thread.start()

    # return jsonify({"message": "OK"}), 200
