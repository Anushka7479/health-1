from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client


def broadcast_sms(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                                                "yet? Grab it here: https://www.twilio.com/quest")

    TWILIO_ACCOUNT_SID = 'AC53b8b3ae94c0ab7c5f0706eb8757fbfb'
    TWILIO_AUTH_TOKEN = '18f82984fdf1ce00932b4079d618e93f'
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    #for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
    #    if recipient:
    client.messages.create(to=+918420042422,
                                   from_=+12569603211,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)# Create your views here.
