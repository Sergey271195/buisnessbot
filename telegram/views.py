from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TelegramUser, check_or_create_user, check_or_create_user_with_context
from .TelegrambotPython import TelegramBot
from .keyboards import MAIN_KEYBOARD
from .message_handlers import (handle_news_request, handle_events_request, 
                            handle_service_list_request, handle_service_request, handle_sub_service_request )

import json
import logging
import requests
import re

from .models import TelegramUser

logging.basicConfig(level=logging.INFO)
TELEGRAM_BOT = TelegramBot()

@csrf_exempt
def entrypoint(request):
    logging.info("[TELEGRAM ENTRYPOINT]")
    try:
        request_body = json.loads(request.body)
        print(request_body)
        message = request_body.get('message')
        callback_query = request_body.get('callback_query')
        if message:
            logging.info("[TELEGRAM ENTRYPOINT] INCOMING TEXT MESSAGE")
            message_text = message.get('text')
            user = message.get('from')
            entities = message.get('entities')
            if entities:
                handle_bot_commands(message_text = message_text, user = user)
            else:
                handle_text_messages(message_text = message_text, user = user)
        elif callback_query:
            logging.info("[TELEGRAM ENTRYPOINT] INCOMING CALLBACK QUERY")
            user = callback_query.get('from')
            data = callback_query.get('data')
            message_id = callback_query.get('message').get('message_id')
            handle_callback_query(user = user, data = data, message_id = message_id)
    except Exception as e:
        logging.warning("[TELEGRAM ENTRYPOINT] ERROR WHILE RECIEVING REQUESTS TO ENTRYPOINT")
        logging.warning(e)

    return JsonResponse({'STATUS_CODE': 200})

@csrf_exempt
def send_message_to_users(request):
    json_body = json.loads(request.body)
    message = json_body.get("message")
    users = json_body.get("users")
    if message and isinstance(users, list):
        for user_id in users:
            try:
                TELEGRAM_BOT.send_text_message_to_id(message = message, telegram_id = user_id)
                logging.info(f"[TELEGRAM] SENDING TEXT MESSAGE FROM ADMIN PANEL. SUCCESSFULLY SEND MESSAGE {message} TO USER {user_id}")
            except Exception as e:
                logging.info(f"[TELEGRAM] SENDING TEXT MESSAGE FROM ADMIN PANEL. EXCEPTION WHILE SENDING MESSAGE TO USER {user_id}")
                logging.info(e)
        return JsonResponse({"STATUS_CODE": 200})
    else:
        return JsonResponse({"STATUS_CODE": 400, "MESSAGE": "WRONG REQUEST PARAMETERS"})

def test_send_message(request):
    request = requests.post('https://bot.xn--37-9kcqjffxnf3b.xn--p1ai/telegram/send', json = 
        {"message": "Откуда я шлю сообщения?", "users": [540863534]}
    )
    print(request)
    return JsonResponse({"STATUS_CODE": 200})

def handle_text_messages(message_text, user):
    logging.info("[TELEGRAM ENTRYPOINT] TEXT MESSAGE")
    user = check_or_create_user(request_user = user)
    try:
        TELEGRAM_BOT.send_text_message(
                message = 'Воспользуйтесь клавиатурой для получения актуальной информации',
                user = user,
                keyboard = MAIN_KEYBOARD,
            )
        logging.info("[TELEGRAM ENTRYPOINT] SUCCESSFULLY REPLIED TO TEXT MESSAGE")
    except Exception as e:
        logging.info("[TELEGRAM ENTRYPOINT] EXCEPTION WHILE REPLING TO TEXT MESSAGE")
        logging.info(e)

def handle_bot_commands(message_text, user):
    logging.info("[TELEGRAM ENTRYPOINT] BOT COMMAND")
    if '/start' in message_text:
        logging.info("[TELEGRAM ENTRYPOINT] START BOT COMMAND")
        try:
            user_info = message_text.replace('/start', '').strip()
            logging.info(f"[TELEGRAM ENTRYPOINT] CHECKING USER WITH USER INFO {user_info}")
            user = check_or_create_user_with_context(request_user = user, user_info = user_info)
        except Exception as e:
            logging.info("[TELEGRAM ENTRYPOINT] WRONG PARAMETERS WITH REQUEST. UNABLE TO GET BITRIX_ID")
            user = check_or_create_user(request_user = user)
        TELEGRAM_BOT.send_text_message(
                message = 'Воспользуйтесь клавиатурой для получения актуальной информации',
                user = user,
                keyboard = MAIN_KEYBOARD,
            )

def handle_callback_query(user, data, message_id):
    logging.info("[TELEGRAM ENTRYPOINT] CALLBACK QUERY")
    user = check_or_create_user(request_user = user)

    if 'illuminator_NEWS' in data:
        logging.info("[TELEGRAM ENTRYPOINT] HANDLING NEWS REQUEST")
        if '$' in data:
            try:
                page = int(data.split('$')[1])
                handle_news_request(user = user, message_id = message_id, page = page)
            except Exception as e:
                logging.info("[TELEGRAM ENTRYPOINT] EXCEPTION WHILE HANDLING NEWS REQUEST")
                logging.info(e)
        else:
            handle_news_request(user = user, message_id = message_id)
    
    elif 'illuminator_EVENTS' in data:
        logging.info("[TELEGRAM ENTRYPOINT] HANDLING EVENTS REQUEST")
        if '$' in data:
            try:
                page = int(data.split('$')[1])
                handle_events_request(user = user, message_id = message_id, page = page)
            except Exception as e:
                logging.info("[TELEGRAM ENTRYPOINT] EXCEPTION WHILE HANDLING EVENTS REQUEST")
                logging.info(e)
        else:
            handle_events_request(user = user, message_id = message_id)
    
    elif data == 'illuminator_SERVICES' or data == 'illuminator_BACK_SERVICES':
        handle_service_list_request(user, message_id)
    
    elif 'illuminator_SERVICE' in data:
        handle_service_request(user, message_id, data)
    
    elif 'illuminator_SUBSERVICE' in data:
        handle_sub_service_request(user, message_id, data)

    else:
        TELEGRAM_BOT.edit_text_message(
                        message_update = 'Воспользуйтесь клавиатурой для получения актуальной информации',
                        user = user,
                        keyboard = MAIN_KEYBOARD,
                        message_id = message_id,
                    )