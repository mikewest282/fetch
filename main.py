from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/fetch", methods=["GET"])
def fetch_value():
    try:
        response = requests.get("http://11z.co/_w/16202/selection")
        response.raise_for_status()
        data = response.json()
        return jsonify({"value": data.get("value", "No value found")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
