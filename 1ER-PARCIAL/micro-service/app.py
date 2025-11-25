from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "server": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    print("Starting time service...")
    app.run(host="0.0.0.0", port=5000)
