from flask import Flask, request
import requests
import os

TOKEN = os.getenv("8551489067:AAFebfBblzCwjQ5f81O3WiSGjkfxPdU9VbI")
URL = f"https://api.telegram.org/bot{8551489067:AAFebfBblzCwjQ5f81O3WiSGjkfxPdU9VbI}/"

app = Flask(__name__)

def sendMessage(chat_id, text):
    requests.post(URL + "sendMessage", json={"chat_id": chat_id, "text": text})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        sendMessage(chat_id, f"Você disse: {text}")
    return "ok", 200

@app.route('/')
def index():
    return "Bot rodando", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
