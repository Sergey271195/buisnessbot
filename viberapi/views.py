from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ViberUser, check_or_create_user
from .ViberbotPython import ViberBot

import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = '4c783b57e380086b-c90dda0abe0e8ebe-7a99acd0bb05c2de'
HEADERS = {'X-Viber-Auth-Token': TOKEN}
HOST_URL = 'https://5d9da2d96a4f.ngrok.io'
RESOURCE_WEBHOOK_URL = 'https://chatapi.viber.com/pa/set_webhook'
VIBER_BOT = ViberBot()


def create_webhook(request):
    response = VIBER_BOT.create_webhook()
    return JsonResponse(response)


def remove_webhook(request):
    response = VIBER_BOT.remove_webhook()
    return JsonResponse(response)


def handle_text_message(user, message):
    message_text = message.get('text')
    logging.info(f"[HANDLE TEXT MESSAGE] RECIEIVING MESSAGE: '{message_text}'")

    if message_text == 'NEWS':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Запрос на получение списка новостей...',
            keyboard = True
        )

    elif message_text == 'EVENTS':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Запрос на получение списка мероприятий...',
            keyboard = True
        )

    elif message_text == 'SERVICES':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Запрос на получение списка услуг...',
            keyboard = True
        )

    else:
        VIBER_BOT.send_text_message(
            receiver = user, 
            message = 'Воспользуйтесь клавиатурой для получения актуальной информации',
            keyboard = True
        )


def handle_message(request_body):
    user = check_or_create_user(request_body.get('sender')) # Think if this one is necessary
    message = request_body.get('message')
    if message:
        message_type = message.get('type')
        if message_type == 'text':
            handle_text_message(user = user, message = message)

def handle_conversation_start(request_body):
    user = check_or_create_user(request_body.get('user'))



def broadcast_message(message):
    users = ViberUser.objects.all()
    ids = [user.viber_id for user in users]
    VIBER_BOT.broadcast_message(message = message, ids = ids)


@csrf_exempt
def entrypoint(request):
    logging.info("[ENTRYPOINT]")
    request_body = json.loads(request.body)
    event = request_body.get('event')

    if event:
        if event == 'conversation_started':
            handle_conversation_start(request_body)
            return JsonResponse({'STATUS_CODE': 200})

        if event == 'message':
            handle_message(request_body)
            return JsonResponse({'STATUS_CODE': 200})

    return JsonResponse({'STATUS_CODE': 200}) 
      

