from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# POST /api/order
@app.route("/api/order", methods=["POST"])
def make_order():
    data = request.json

    # Basic validation
    if not data or "car" not in data or "name" not in data or "phone" not in data:
        return jsonify({"message": "Missing fields"}), 400

    orders_file = "/tmp/orders.json"

    # Load existing orders
    if os.path.exists(orders_file):
        with open(orders_file, "r", encoding="utf-8") as f:
            orders = json.load(f)
    else:
        orders = []

    # Add timestamp
    data["timestamp"] = datetime.now().isoformat()
    orders.append(data)

    # Save
    with open(orders_file, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

    return jsonify({"message": "Your order has been saved!"})

# Health check
@app.route("/")
def home():
    return jsonify({"message": "API is running"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
