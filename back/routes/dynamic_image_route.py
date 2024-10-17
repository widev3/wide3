# from flask import Blueprint, send_file
# from PIL import Image, ImageDraw
# import io

# # Define the blueprint for this route
# dynamic_image_blueprint = Blueprint("dynamic_image", __name__)


# # Route for returning a dynamically generated image
# @dynamic_image_blueprint.route("/dynamic-image", methods=["GET"])
# def get_dynamic_image():
#     # Create an image with Pillow
#     img = Image.new("RGB", (200, 100), color=(73, 109, 137))
#     d = ImageDraw.Draw(img)
#     d.text((10, 10), "Hello, World!", fill=(255, 255, 0))

#     # Save to a BytesIO object to serve as a response
#     img_io = io.BytesIO()
#     img.save(img_io, "JPEG")
#     img_io.seek(0)

#     return send_file(img_io, mimetype="image/jpeg")
