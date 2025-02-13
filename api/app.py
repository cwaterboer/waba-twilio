from fastapi import FastAPI, Form
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.post("/api/whatsapp")
async def whatsapp_webhook(Body: str = Form(...)):
    resp = MessagingResponse()
    reply = resp.message()

    if "hello" in Body.lower():
        reply.body("Hey! How can I assist you?")
    else:
        reply.body("I'm an automated bot!")

    return str(resp)