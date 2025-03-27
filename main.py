from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    print("Responding to message:", incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Привет! Это Lumi. Я с тобой.")
    return str(resp)


