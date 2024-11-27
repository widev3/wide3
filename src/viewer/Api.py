import json
import threading
from flask import Flask, jsonify, request

api_server = Flask(__name__)


class Api:
    _viewer_setup_callback = None
    _viewer_add_callback = None

    def viewer_setup_callback(self, func):
        Api._viewer_setup_callback = func

    def viewer_add_callback(self, func):
        Api._viewer_add_callback = func

    def run(self, port):
        def run_server():
            api_server.run(port=port, debug=False, use_reloader=False)

        server_thread = threading.Thread(target=run_server)
        server_thread.daemon = True
        server_thread.start()

    @api_server.route("/viewer/setup", methods=["GET"])
    def slice_get():
        Api._viewer_setup_callback() if Api._viewer_setup_callback else None
        return jsonify({"code": "OK"}), 200

    @api_server.route("/viewer/add", methods=["POST"])
    def slice_post():
        if request.is_json:
            data = request.get_json()
            python_dict = json.loads(data)
            timestamp = data["timestamp"]
            slice = data["slice"]
            Api._viewer_add_callback() if Api._viewer_add_callback else None
            return jsonify({"code": "OK"}), 200
        else:
            return jsonify({"error": "Request must be in JSON format"}), 400
