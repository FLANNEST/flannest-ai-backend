from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = "APNI_API_KEY_YAHAN_DALO"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + OPENROUTER_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/free",
            "messages": data.get("messages", [])
        }
    )

    return jsonify(response.json())

@app.route("/")
def home():
    return "FLANNEST AI Backend is Online!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
