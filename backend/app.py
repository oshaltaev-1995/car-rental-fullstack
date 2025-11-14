from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json, os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path=""
)
CORS(app)

# API
@app.post("/api/order")
def make_order():
    data = request.json
    if not data or "car" not in data or "name" not in data or "phone" not in data:
        return jsonify({"message": "Missing fields"}), 400

    path = "/tmp/orders.json"
    orders = json.load(open(path)) if os.path.exists(path) else []
    data["timestamp"] = datetime.now().isoformat()
    orders.append(data)
    json.dump(orders, open(path, "w"), indent=2)

    return jsonify({"message": "Your order has been saved!"})

# SPA fallback
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_spa(path):
    full_path = os.path.join(FRONTEND_DIR, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(FRONTEND_DIR, path)
    return send_from_directory(FRONTEND_DIR, "index.html")
