# flask_random_temp.py
from flask import Flask, jsonify
import threading
import random
import time

app = Flask(__name__)

# Store latest temperature
latest_data = {"id": 1, "temperature": None}

# Background function to update temperature randomly
def update_temperature():
    while True:
        latest_data["temperature"] = round(random.uniform(20.0, 40.0), 2)
        time.sleep(2)  # update every 2 seconds

# API endpoint to provide the latest temperature
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    # Start the background thread to update temperature
    threading.Thread(target=update_temperature, daemon=True).start()
    
    # Run the Flask server
    app.run(host="0.0.0.0", port=5000)