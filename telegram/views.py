from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TelegramUser, check_or_create_user, check_or_create_user_with_context
from .TelegrambotPython import TelegramBot
from .keyboards import (MAIN_KEYBOARD, SERVICES_KEYBOARD, PROMOTION_KEYBOARD,
                        PERFOMANCE_KEYBOARD, TECH_SUPPORT_KEYBOARD, FINANCIAL_SUPPORT_KEYBOARD,
                        AGRICULTURE_KEYBOARD, EXPORT_KEYBOARD )
import json
import logging

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
            bitrix_id = int(message_text.replace('/start', ''))
            logging.info(f"[TELEGRAM ENTRYPOINT] CHECKING USER WITH BITRIX_ID {bitrix_id}")
            user = check_or_create_user_with_context(request_user = user, bitrix_id = bitrix_id)
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

    if data == 'illuminator_NEWS':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            message_update = 'Получение акутальных новостей...',
            user = user,
            keyboard = MAIN_KEYBOARD,
        )
    
    elif data == 'illuminator_EVENTS':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            message_update = 'Получение акутальных мероприятий...',
            user = user,
            keyboard = MAIN_KEYBOARD,
        )
    
    elif data == 'illuminator_SERVICES' or data == 'illuminator_BACK_SERVICES':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            message_update = 'Доступные меры поддержки',
            user = user,
            keyboard = SERVICES_KEYBOARD,
        )

    elif data == 'illuminator_PROMOTION':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            message_update = 'Меры поддержки. Продвижение',
            user = user,
            keyboard = PROMOTION_KEYBOARD,
        )
    
    elif data == 'illuminator_PERFOMANCE':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            user = user,
            message_update = 'Меры поддержки. Производительность труда',
            keyboard = PERFOMANCE_KEYBOARD
        )

    elif data == 'illuminator_TECH_CONNECTION':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            user = user,
            message_update = 'Меры поддержки. Техприсоединение',
            keyboard = TECH_SUPPORT_KEYBOARD
        )

    elif data == 'illuminator_FINANCIAL_SUPPORT':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            user = user,
            message_update = 'Меры поддержки. Финансовая поддержка',
            keyboard = FINANCIAL_SUPPORT_KEYBOARD
        )
    
    elif data == 'illuminator_AGRICULTURE':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            user = user,
            message_update = 'Меры поддержки. Сельское хозяйство',
            keyboard = AGRICULTURE_KEYBOARD
        )

    elif data == 'illuminator_EXPORT':
        TELEGRAM_BOT.edit_text_message(
            message_id = message_id,
            user = user,
            message_update = 'Меры поддержки. Экспорт',
            keyboard = EXPORT_KEYBOARD
        )

    else:
        TELEGRAM_BOT.edit_text_message(
                message_id = message_id,
                message_update = 'Воспользуйтесь клавиатурой для получения актуальной информации',
                user = user,
                keyboard = MAIN_KEYBOARD,
            )

