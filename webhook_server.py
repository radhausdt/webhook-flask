from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Received TradingView Webhook:", data)
    
    # Optional: You can log it or send to Telegram/MT5 from here
    
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run()
