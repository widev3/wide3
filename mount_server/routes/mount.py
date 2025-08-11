import math
import threading
from Mount import Mount
from astropy import units
from flask import request, jsonify, Blueprint
from astropy.coordinates import EarthLocation

mount_bp = Blueprint("mount", __name__)

mount = Mount(
    EarthLocation(
        lat=19.8207 * units.deg, lon=-155.4681 * units.deg, height=4205 * units.m
    )
)


@mount_bp.route("/", methods=["POST"])
def mount_root():
    def background_move():
        global mount
        mount.move()

    global mount
    if mount.is_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()

    if "target" not in data:
        return jsonify({"error": "Missing required field: target"}), 400

    target = data["target"]
    if not target:
        return jsonify({"error": "Missing required field: target"}), 400

    if "ra" in target and "dec" not in target:
        return jsonify({"error": "Missing required field: target.dec"}), 400

    if "dec" in target and "ra" not in target:
        return jsonify({"error": "Missing required field: target.dec"}), 400

    if "alt" in target and "az" not in target:
        return jsonify({"error": "Missing required field: target.az"}), 400

    if "az" in target and "alt" not in target:
        return jsonify({"error": "Missing required field: target.el"}), 400

    if "ra" in target and "az" in target:
        return jsonify({"error": "Target should be ar-dec or al-az only"}), 400

    if "az" in target:
        alt = target["alt"] * units.deg
        az = target["az"] * units.deg
        mount.set_altaz_target(alt, az)

    if "ra" in target:
        ra = target["ra"] * units.deg
        dec = target["dec"] * units.deg
        mount.set_radec_target(ra, dec)

    if "offset" in data:
        offset = data["offset"]
        if offset:
            if ("ra" in offset or "dec" in offset) and not (
                "az" in offset or "alt" in offset
            ):
                if "ra" in offset:
                    ra = offset["ra"]
                    mount.set_ra_offset(ra)

                if "dec" in offset:
                    dec = offset["dec"]
                    mount.set_dec_offset(dec)
            elif ("az" in offset or "alt" in offset) and not (
                "ra" in offset or "dec" in offset
            ):
                if "az" in offset:
                    az = offset["az"]
                    mount.set_az_offset(az)

                if "alt" in offset:
                    alt = offset["alt"]
                    mount.set_alt_offset(alt)
            else:
                return jsonify({"error": "Cannot set offset"}), 400

    if "behavior" in data:
        behavior = data["behavior"]
        if behavior not in ["follow", "transit", "towards"]:
            return jsonify({"error": f"Invalid behavior {behavior}"}), 400

        mount.set_behavior(behavior)

    thread = threading.Thread(target=background_move)
    thread.start()

    return jsonify({"message": "OK"}), 200


@mount_bp.route("/location", methods=["POST"])
def mount_location():
    def is_strict_float(value: str) -> bool:
        try:
            f = float(value)
            return math.isfinite(f)
        except ValueError:
            return False

    global mount
    if mount.is_moving():
        return jsonify({"error": "Already moving"}), 403

    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty body"}), 400

    if "lat" not in data:
        return jsonify({"error": "Missing required field: lat"}), 400

    if not data["lat"] or not is_strict_float(data["lat"]):
        return jsonify({"error": "Invalid value. Must be a number"}), 400

    if "lon" not in data:
        return jsonify({"error": "Missing required field: lon"}), 400

    if not data["lon"] or not is_strict_float(data["lon"]):
        return jsonify({"error": "Invalid value. Must be a number"}), 400

    if "height" not in data:
        return jsonify({"error": "Missing required field: height"}), 400

    if not data["height"] or not is_strict_float(data["height"]):
        return jsonify({"error": "Invalid value. Must be a number"}), 400

    mount = Mount(
        EarthLocation(
            lat=data["lat"] * units.deg,
            lon=data["lon"] * units.deg,
            height=data["height"] * units.m,
        )
    )

    return jsonify({"message": "OK"}), 200
