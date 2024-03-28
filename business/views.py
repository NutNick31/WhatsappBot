from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from .functions import *

# Create your views here.

def home(request):
    return render(request, 'business/index.html', {})

@csrf_exempt
def whatsappWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = '3769a501-51d1-432e-873e-1c223dc3bcb7'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        # mode = 'hello'
        # token = 'hello'
        # challenge = 'hello'

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)
    
    # if request.method == 'POST':
    #     data = json.loads(request.body)

    #     return HttpResponse('success', status=200)
        
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'object' in data and 'entry' in data:
            if data['object'] == 'whatsapp_business_account':
                try:
                    for entry in data['entry']:
                        phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        messageId = entry['changes'][0]['value']['messages'][0]['id']
                        timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body']

                        phoneNumber = "917249222539"
                        message = 'Hello, Dear user, \n {} was recieved'.format(text)
                        sendWhatsAppMessage(phoneNumber,message)
                except:
                    pass
        return HttpResponse('success', status=200)