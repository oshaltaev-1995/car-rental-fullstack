from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # permit cross-origin requests for frontend-backend communication

# ==== POST /order ====
@app.route("/order", methods=["POST"])
def make_order():
    data = request.json
    if not data or "car" not in data or "name" not in data or "phone" not in data:
        return jsonify({"message": "Missing fields"}), 400

    # create or read orders.json
    orders_file = "/tmp/orders.json"
    if os.path.exists(orders_file):
        with open(orders_file, "r", encoding="utf-8") as f:
            orders = json.load(f)
    else:
        orders = []

    # Adding timestamp and saving the order
    data["timestamp"] = datetime.now().isoformat()
    orders.append(data)

    with open(orders_file, "w", encoding="utf-8") as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)

    return jsonify({"message": "Your order has been saved!"})

# Test route
@app.route("/")
def home():
    return jsonify({"message": "Car Rental Order API is running."})

if __name__ == "__main__":
    app.run()


