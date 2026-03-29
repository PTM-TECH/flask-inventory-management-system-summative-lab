from flask import Flask, request, jsonify
import inventory

# Initialize Flask app
app = Flask(__name__)  

# Route: GET /inventory
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory.get_all_items())

# Route: GET /inventory/<id>
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = inventory.get_item(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Route: POST /inventory
@app.route("/inventory", methods=["POST"])
def create_item():
    data = request.json
    item = inventory.add_item(
        data["name"],
        data["brand"],
        data["price"],
        data["stock"],
        data["barcode"]
    )
    return jsonify(item), 201

# Route: PATCH /inventory/<id>
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    updates = request.json
    item = inventory.update_item(item_id, updates)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Route: DELETE /inventory/<id>
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    success = inventory.delete_item(item_id)
    if not success:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)