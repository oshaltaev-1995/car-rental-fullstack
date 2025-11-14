from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime

# Import DB helper functions
from db import init_db, insert_order, get_all_orders

# Initialize SQLite database
init_db()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app)

# --- API ---

@app.post("/api/order")
def make_order():
    data = request.json

    if not data or "car" not in data or "name" not in data or "phone" not in data:
        return jsonify({"message": "Missing fields"}), 400

    timestamp = datetime.now().isoformat()

    insert_order(
        data["car"],
        data["name"],
        data["phone"],
        timestamp
    )

    return jsonify({"message": "Your order has been saved!"})


@app.get("/api/orders")
def list_orders():
    return jsonify(get_all_orders())


# --- SPA fallback ---
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_spa(path):
    full_path = os.path.join(FRONTEND_DIR, path)

    if path != "" and os.path.exists(full_path):
        return send_from_directory(FRONTEND_DIR, path)

    return send_from_directory(FRONTEND_DIR, "index.html")


if __name__ == "__main__":
    app.run(debug=True)
