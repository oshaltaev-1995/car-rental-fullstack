import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "orders.db")


def init_db():
    os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car TEXT NOT NULL,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def insert_order(car, name, phone, timestamp):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (car, name, phone, timestamp) VALUES (?, ?, ?, ?)",
        (car, name, phone, timestamp)
    )
    conn.commit()
    conn.close()


def get_all_orders():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, car, name, phone, timestamp FROM orders")
    rows = cur.fetchall()
    conn.close()

    return [
        {"id": r[0], "car": r[1], "name": r[2], "phone": r[3], "timestamp": r[4]}
        for r in rows
    ]
