from twilio.rest import Client


TWILIO_SID = "AC7d73be5d658c6cecb2c54d5e62b28557"
TWILIO_AUTH_TOKEN = "243999bc62e820cbe8ad99123fecc48c"
TWILIO_VIRTUAL_NUMBER = "+13074481980"
TWILIO_VERIFIED_NUMBER = "+5511962246633"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
