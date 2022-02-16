from twilio.rest import Client

TWILIO_SID = "AC7d73be5d658c6cecb2c54d5e62b28557"
TWILIO_AUTH_TOKEN = "243999bc62e820cbe8ad99123fecc48c"
TWILIO_VIRTUAL_NUMBER = "+13074481980"
TWILIO_VERIFIED_NUMBER = "+5511962246633"

class GerenciadorNotificacao:

    def __init__(self):

        self.cliente = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def mandar_msn(self, mensagem):

        self.cliente.messages.create(
            body=mensagem,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

