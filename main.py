from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Webhook je aktivní!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and "action" in data:
        with open("signal.txt", "w") as f:
            f.write(data["action"])
        return {"status": "success"}, 200
    return {"status": "invalid request"}, 400

@app.route('/signal.txt', methods=['GET'])
def get_signal():
    try:
        with open("signal.txt", "r") as f:
            return f.read(), 200
    except FileNotFoundError:
        return "No signal yet", 200

# ⛳️ Spuštění vždy – i mimo __main__ (Render to vyžaduje)
port = int(os.environ.get("PORT", 5000))
print(f"✅ Running on 0.0.0.0:{port}")
app.run(host="0.0.0.0", port=port, debug=False)




