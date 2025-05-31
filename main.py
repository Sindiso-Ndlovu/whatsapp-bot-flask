from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def reply_whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Basic logic
    if "hello" in incoming_msg:
        msg.body("Hi there! 👋 This is your WhatsApp bot speaking.")
    else:
        msg.body("I didn't understand that. Type 'hello' to greet me!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
