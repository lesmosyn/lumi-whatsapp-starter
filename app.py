from flask import Flask, request

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    return f"Lumi received: {incoming_msg}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

