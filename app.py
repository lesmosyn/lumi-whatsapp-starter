from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    reply = f"Lumi received: {incoming_msg}"
    return Response(reply, status=200)
