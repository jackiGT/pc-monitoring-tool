from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app

@app.route("/monitor/data", methods=["POST"])
def recieveData():
    print("Check to see if method ran")
    payload = request.get_json()

    print(f"Recieved data from {payload['deviceID']}")
    print(f"CPU: {payload['cpu']['CPU %']}")

    return jsonify({"status": "success", "message": "data recieved"}), 200

if __name__ == "__main__":
    print("Server is listening on http://127.0.0.1:5000...")
    app.run(debug=True, port=5000)

