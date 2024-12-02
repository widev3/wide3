import json
import threading
from flask import Flask, jsonify, request

api_server = Flask(__name__)


class Api:
    _viewer_setup_callback = None
    _viewer_add_callback = None

    def run(self, port):
        def run_server():
            api_server.run(port=port, debug=False, use_reloader=False)

        server_thread = threading.Thread(target=run_server)
        server_thread.daemon = True
        server_thread.start()

    @api_server.route("/viewer/ping", methods=["GET"])
    def viewer_ping():
        return jsonify({"code": "OK"}), 200

    @api_server.route("/viewer/setup", methods=["GET"])
    def viewer_setup():
        Api._viewer_setup_callback() if Api._viewer_setup_callback else None
        return jsonify({"code": "OK"}), 200

    @api_server.route("/viewer/add", methods=["POST"])
    def viewer_add():
        if request.is_json:
            arr = request.get_json()
            arr = json.loads(arr)
            res = Api._viewer_add_callback(arr) if Api._viewer_add_callback else None
            if res:
                return jsonify({"code": "OK"}), 200
            else:
                return jsonify({"code": "unauthorized"}), 200
        else:
            return jsonify({"error": "Request must be in JSON format"}), 400
