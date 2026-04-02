from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse 
from groq import Groq 
from pyngrok import ngrok
import os
from dotenv import load_dotenv

load_dotenv()

ngrok.set_auth_token(os.getenv("NGROK_AUTHTOKEN"))
ngrok.kill()  # kill any old tunnels first
public_url = ngrok.connect(5000)
print(f"your public url is: {public_url}")

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_message = request.form.get("Body")
    print(f"Received: {incoming_message}")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content":"you are acting as dany. be energetic and funny with your replies and ask questions back occassionally",
            },
                {"role": "user",
                "content": incoming_message}
        ]
    )

    reply = response.choices[0].message.content
    print(f"replying: {reply}")

    twilio_response = MessagingResponse()
    twilio_response.message(reply)
    return str(twilio_response)

if __name__ == "__main__":
    app.run(debug=False)