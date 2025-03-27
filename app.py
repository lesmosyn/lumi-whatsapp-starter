@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    # Здесь должна быть логика генерации ответа
    resp = MessagingResponse()
    msg = resp.message()
    msg.body("Hello, this is Lumi speaking!")
    return str(resp)



