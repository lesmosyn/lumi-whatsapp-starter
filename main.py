from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    print("Получено сообщение:", incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()
    print("Отправляем ответ Lumi!")
    msg.body("Hello, this is Lumi speaking!")
    
    return str(resp)


