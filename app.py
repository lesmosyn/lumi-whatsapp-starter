from flask import Flask, request
from os import environ

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').lower()
    return f'Lumi received: {incoming_msg}'

if __name__ == '__main__':
    port = int(environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
 
