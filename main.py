from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_auto_responder():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg or 'hi' in incoming_msg:
        msg.body("👋 Hello Sindiso! Welcome to our smart auto-responder.\n\nType:\n1️⃣ for Pricing\n2️⃣ for Location\n3️⃣ for Contact Info")
    elif incoming_msg == '1':
        msg.body("💰 Our services start at just $10/month for your own chatbot.")
    elif incoming_msg == '2':
        msg.body("📍 We’re based in Harare CBD, near Joina City.")
    elif incoming_msg == '3':
        msg.body("📞 You can reach us on +263 71 234 5678 or reply 'contact me'.")
    else:
        msg.body("❓ I didn't get that. Please type 'hello' to see menu options.")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
