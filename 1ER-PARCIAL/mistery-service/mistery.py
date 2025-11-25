from flask import Flask, jsonify
import requests
import threading
import os

app = Flask(__name__)

entries_env = os.getenv("ENTRIES", "s1:5000,s2:5000,s3:5000")
ENTRIES= [f"http://{b}" for b in entries_env.split(",")]

index = 0
lock = threading.Lock()

def get_next_entry():
    global index
    with lock:
        entry = ENTRIES[index]
        index = (index + 1) % len(ENTRIES)
        return entry

@app.route("/", methods=["GET"])
def dowork():
    next = get_next_entry()
    try:
        resp = requests.get(next, timeout=2)
        return resp.json(), resp.status_code
    except Exception as e:
        return jsonify({"error": f"Entry {next} unreachable", "details": str(e)}), 503

if __name__ == "__main__":
    print("Starting mistery...")
    app.run(host="0.0.0.0", port=8000)
