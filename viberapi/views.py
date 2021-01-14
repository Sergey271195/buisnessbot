from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ViberUser, check_or_create_user, check_or_create_user_with_context
from .ViberbotPython import ViberBot
from telegram.TelegrambotPython import TelegramBot
from .keyboards import (MAIN_KEYBOARD, SERVICES_KEYBOARD, PROMOTION_KEYBOARD,
                        PERFOMANCE_KEYBOARD, TECH_SUPPORT_KEYBOARD, FINANCIAL_SUPPORT_KEYBOARD,
                        AGRICULTURE_KEYBOARD, EXPORT_KEYBOARD )

import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = '4c783b57e380086b-c90dda0abe0e8ebe-7a99acd0bb05c2de'
HEADERS = {'X-Viber-Auth-Token': TOKEN}
HOST_URL = 'https://5d9da2d96a4f.ngrok.io'
RESOURCE_WEBHOOK_URL = 'https://chatapi.viber.com/pa/set_webhook'
VIBER_BOT = ViberBot()
TELEGRAM_BOT = TelegramBot()


def create_webhook(request):
    viber_response = VIBER_BOT.create_webhook()
    telegram_response = TELEGRAM_BOT.create_webhook()
    return JsonResponse(viber_response)


def remove_webhook(request):
    viber_response = VIBER_BOT.remove_webhook()
    telegram_response = TELEGRAM_BOT.remove_webhook()
    return JsonResponse(viber_response)


def handle_text_message(user, message):
    message_text = message.get('text')
    logging.info(f"[HANDLE TEXT MESSAGE] RECIEIVING MESSAGE: '{message_text}'")

    if message_text == 'illuminator_NEWS':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Запрос на получение списка новостей...',
            keyboard = MAIN_KEYBOARD
        )

    elif message_text == 'illuminator_EVENTS':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Запрос на получение списка мероприятий...',
            keyboard = MAIN_KEYBOARD
        )

    elif message_text == 'illuminator_SERVICES':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Доступные меры поддержки',
            keyboard = SERVICES_KEYBOARD
        )

    elif message_text == 'illuminator_PROMOTION':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Продвижение',
            keyboard = PROMOTION_KEYBOARD
        )

    elif message_text == 'illuminator_BACK_SERVICES':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Продвижение',
            keyboard = SERVICES_KEYBOARD
        )

    elif message_text == 'illuminator_PERFOMANCE':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Производительность труда',
            keyboard = PERFOMANCE_KEYBOARD
        )

    elif message_text == 'illuminator_TECH_CONNECTION':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Техприсоединение',
            keyboard = TECH_SUPPORT_KEYBOARD
        )

    elif message_text == 'illuminator_FINANCIAL_SUPPORT':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Финансовая поддержка',
            keyboard = FINANCIAL_SUPPORT_KEYBOARD
        )
    
    elif message_text == 'illuminator_AGRICULTURE':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Сельское хозяйство',
            keyboard = AGRICULTURE_KEYBOARD
        )

    elif message_text == 'illuminator_EXPORT':
        VIBER_BOT.send_text_message(
            receiver = user,
            message = 'Меры поддержки. Экспорт',
            keyboard = EXPORT_KEYBOARD
        )

    else:
        VIBER_BOT.send_text_message(
            receiver = user, 
            message = 'Воспользуйтесь клавиатурой для получения актуальной информации',
            keyboard = MAIN_KEYBOARD
        )


def handle_message(request_body):
    user = check_or_create_user(request_body.get('sender')) # Think if this one is necessary
    message = request_body.get('message')
    if message:
        message_type = message.get('type')
        if message_type == 'text':
            handle_text_message(user = user, message = message)

def handle_conversation_start(request_body):
    context = request_body.get('context')
    if context:
        user = check_or_create_user_with_context(request_body.get('user'), context = context)
    else:
        user = check_or_create_user(request_body.get('user'))
    handle_text_message(user = user, message = {'message_text': ''})



def broadcast_message(message):
    users = ViberUser.objects.all()
    ids = [user.viber_id for user in users]
    VIBER_BOT.broadcast_message(message = message, ids = ids)


@csrf_exempt
def entrypoint(request):
    logging.info("[VIBER ENTRYPOINT]")
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


@csrf_exempt
def send_text_message(request):
    json_body = json.loads(request.body)
    message = json_body.get("message")
    users = json_body.get("users")
    if message and isinstance(users, list):
        try:
            VIBER_BOT.broadcast_message(message = message, ids = users)
            logging.info(f"[VIBER] BROADCATING MESSAGE FROM ADMIN PANEL. SUCCESSFULLY SEND MESSAGE {message} TO USER {users}")
        except Exception as e:
            logging.info(f"[VIBER] BROADCATING MESSAGE FROM ADMIN PANEL. EXCEPTION WHILE SENDING MESSAGE TO USER {users}")
            logging.info(e)
        return JsonResponse({"STATUS_CODE": 200})
    else:
        return JsonResponse({"STATUS_CODE": 400, "MESSAGE": "WRONG REQUEST PARAMETERS"})

def test_send_message(request):
    request = requests.post('http://127.0.0.1:8000/viber/send', json = 
        {"message": "Откуда я шлю сообщения?", "users": ["4qCEzNFHzLwykk7qTLMILA=="]}
    )
    print(request)
    return JsonResponse({"STATUS_CODE": 200})
      

