# from flask import Blueprint, send_file

# # Define the blueprint for this route
# image_blueprint = Blueprint("image", __name__)


# # Route for returning a static image
# @image_blueprint.route("/image", methods=["GET"])
# def get_image():
#     image_path = "path/to/your/image.jpg"
#     try:
#         return send_file(image_path, mimetype="image/jpeg")
#     except Exception as e:
#         return str(e), 404
