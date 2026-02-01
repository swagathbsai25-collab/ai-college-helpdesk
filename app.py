from flask import Flask, request, jsonify, send_from_directory
import json
import random
import os

app = Flask(__name__)

# Load intents.json
with open("intents.json", encoding="utf-8") as f:
    intents = json.load(f)

def get_response(user_input):
    user_input = user_input.lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])
    return "Sorry, I didn't understand that. Please try again."

@app.route("/")
def home():
    return send_from_directory('.', 'index.html')

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form.get("msg")
    reply = get_response(user_msg)
    return jsonify({"response": reply})

@app.route("/style.css")
def style():
    return send_from_directory('.', 'style.css')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
