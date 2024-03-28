from django.conf import settings
import requests

def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
                "messaging_product": "whatsapp",
                "recipient": "individual",
                "to": phoneNumber,
                "type": "text",
                "text": {"body": message}
              }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()


phoneNumber = "917249222539"
message = "Hello there, \n This is our first message to you from our django application. \n Regards, \n Team CareChatBot"


sendWhatsAppMessage(phoneNumber, message)