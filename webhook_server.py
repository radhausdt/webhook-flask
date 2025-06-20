from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Received TradingView Webhook:", data)
    return jsonify({"status": "received"}), 200
