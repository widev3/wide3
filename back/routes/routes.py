# from flask import Flask, request, jsonify, send_file
# from PIL import Image, ImageDraw
# import io

# # Sample data
# data = [
#     {"id": 1, "name": "Item 1", "description": "This is item 1"},
#     {"id": 2, "name": "Item 2", "description": "This is item 2"},
# ]


# # GET: Retrieve all items
# @app.route("/items", methods=["GET"])
# def get_items():
#     return jsonify(data)


# # GET: Retrieve a specific item by id
# @app.route("/items/<int:item_id>", methods=["GET"])
# def get_item(item_id):
#     item = next((item for item in data if item["id"] == item_id), None)
#     if item:
#         return jsonify(item)
#     return jsonify({"error": "Item not found"}), 404


# # POST: Add a new item
# @app.route("/items", methods=["POST"])
# def add_item():
#     new_item = request.json
#     new_item["id"] = len(data) + 1
#     data.append(new_item)
#     return jsonify(new_item), 201


# # PUT: Update an item by id
# @app.route("/items/<int:item_id>", methods=["PUT"])
# def update_item(item_id):
#     item = next((item for item in data if item["id"] == item_id), None)
#     if item:
#         updated_data = request.json
#         item.update(updated_data)
#         return jsonify(item)
#     return jsonify({"error": "Item not found"}), 404


# # DELETE: Remove an item by id
# @app.route("/items/<int:item_id>", methods=["DELETE"])
# def delete_item(item_id):
#     global data
#     data = [item for item in data if item["id"] != item_id]
#     return jsonify({"message": "Item deleted"}), 200


# @app.route("/dynamic-image", methods=["GET"])
# def get_dynamic_image():
#     img = Image.new("RGB", (200, 100), color=(73, 109, 137))
#     d = ImageDraw.Draw(img)
#     d.text((10, 10), "Hello, World!", fill=(255, 255, 0))

#     img_io = io.BytesIO()
#     img.save(img_io, "JPEG")
#     img_io.seek(0)

#     return send_file(img_io, mimetype="image/jpeg")
