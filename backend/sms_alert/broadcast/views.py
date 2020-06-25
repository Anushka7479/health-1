from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client


def broadcast_sms(request):
    message_to_broadcast = ("Have you played the incredible TwilioQuest "
                                                "yet? Grab it here: https://www.twilio.com/quest")

    TWILIO_ACCOUNT_SID = '##'
    TWILIO_AUTH_TOKEN = '##'
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    #for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
    #    if recipient:
    client.messages.create(to=+918420042422,
                                   from_=###,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)# Create your views here.
