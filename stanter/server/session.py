import uuid
from pathlib import Path
from flask import request, jsonify, Blueprint

session_bp = Blueprint(Path(__file__).stem, __name__)


global session_id
session_id = None


@session_bp.before_request
def middleware():
    global session_id
    token = request.headers.get("Authorization")
    if token and session_id and token != str(session_id):
        return jsonify({"error": "Session already acquired"}), 401
    if token and not session_id:
        return jsonify({"error": "No active session"}), 401
    if not token and request.path != "/session/acquire":
        return jsonify({"error": "Unauthorized"}), 401


@session_bp.route("/acquire", methods=["GET"])
def session_acquire():
    global session_id
    if not session_id:
        session_id = uuid.uuid4()
        return jsonify({"session_id": session_id}), 200

    return jsonify({"message": "session in use"}), 403


@session_bp.route("/release", methods=["GET"])
def session_release():
    global session_id
    if session_id:
        session_id = None
        return jsonify({"message": "OK"}), 200

    return jsonify({"message": "cannot release an empty session"}), 403
