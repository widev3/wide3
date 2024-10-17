from flask import Blueprint, send_file, request, jsonify

spm_reader_blueprint = Blueprint("image", __name__)


# POST: Add a new item
@spm_reader_blueprint.route("/spm_reader", methods=["POST"])
def spm_reader():
    new_item = request.json
    # new_item["id"] = len(data) + 1
    # data.append(new_item)
    return jsonify(new_item), 200
