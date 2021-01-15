from .ViberbotPython import ViberBot
from .keyboards import (create_switch_keyboard, create_dynamic_service_keyboard, 
                        create_dynamic_subservice_keyboard, create_dynamic_subservice_link_keyboard)

from telegram.message_handlers import ( get_callback_data, get_service_name, request_service, 
                                        get_subservice_callback_data, get_events_data_for_page, 
                                        get_news_data_for_page )

import requests
import re
import logging
import json

logging.basicConfig(level=logging.INFO)
VIBER_BOT = ViberBot()

BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai"

def handle_news_request(user_id, page = None):

    response_message, prev_page_num, next_page_num = get_news_data_for_page(page, viber = True)
    response_keyboard = create_switch_keyboard(
            request_type = 'NEWS',
            next_page = next_page_num,
            prev_page = prev_page_num
        )

    logging.info(f'[NEWS REQUEST] SUCCESSFULLY SENDING {page} PAGE RESPONSE')
    if isinstance(response_message, str):
        VIBER_BOT.send_text_message(
            message = response_message,
            viber_id = user_id,
            keyboard = response_keyboard
        )
    else:
        VIBER_BOT.send_rich_media(
            media = response_message,
            viber_id = user_id,
            keyboard = response_keyboard
        )


def handle_events_request(user_id, page = None):

    response_message, prev_page_num, next_page_num = get_events_data_for_page(page, viber = True)
    response_keyboard = create_switch_keyboard(
            request_type = 'EVENTS',
            next_page = next_page_num,
            prev_page = prev_page_num
        )
    logging.info(f'[EVENTS REQUEST] SUCCESSFULLY SENDING {page} PAGE RESPONSE')
    if isinstance(response_message, str):
        VIBER_BOT.send_text_message(
            message = response_message,
            viber_id = user_id,
            keyboard = response_keyboard
        )
    else:
        VIBER_BOT.send_rich_media(
            media = response_message,
            viber_id = user_id,
            keyboard = response_keyboard
        )

def handle_service_list_request(user_id):
    logging.info('[SERVICE LIST REQUEST]')
    request_url = f'{BASE_URL}/api/bot/getServices.php'
    request = requests.get(request_url)
    try:
        response = request.json()
        response_keyboard = create_dynamic_service_keyboard(response)
        response_message = 'Доступные меры поддержки'
        logging.info(f'[SERVICE LIST REQUEST] SUCCESSFULLY SENDING LIST OF SERVICES')
        VIBER_BOT.send_text_message(
            message = response_message,
            viber_id = user_id,
            keyboard = response_keyboard
        )
       
    except Exception as e:
        logging.info(f'[SERVICE LIST REQUEST] EXCEPTION WHILE CREATING SERVICE LIST')
        logging.info(f'{e}')


def handle_service_request(user_id, data):
    service_id = get_callback_data(data)
    service_name = get_service_name(f"{BASE_URL}/api/bot/getServices.php", service_id)
    service_data = request_service(f"{BASE_URL}/api/bot/getServices.php?section={service_id}")
    response_keyboard = create_dynamic_subservice_keyboard(service_data, service_id)
    if service_data:
        logging.info(f'[SERVICE REQUEST] SUCCESSFULLY SENDING SUBSERVICES OF {service_name} SERVICE')
        VIBER_BOT.send_text_message(
            message = "Меры поддержки. " + service_name,
            viber_id = user_id,
            keyboard = response_keyboard
        )
    else:
        logging.info(f'[SERVICE REQUEST] ERROR WHILE SENDING SUBSERVICES OF {service_name} SERVICE')


def handle_sub_service_request(user_id, data):
    subservice_id, service_id = get_subservice_callback_data(data)
    service_name = get_service_name(f"{BASE_URL}/api/bot/getServices.php", service_id)
    subservice_name = get_service_name(f"{BASE_URL}/api/bot/getServices.php?section={service_id}", subservice_id)
    subservice_data = request_service(f"{BASE_URL}/api/bot/getServices.php?subsection={subservice_id}")
    response_keyboard = create_dynamic_subservice_link_keyboard(subservice_data, service_id)
    if subservice_data:
        print(response_keyboard)
        logging.info(f'[SUBSERVICE REQUEST] SUCCESSFULLY SENDING LINKS OF {subservice_name} SUBSERVICE')
        VIBER_BOT.send_text_message(
            message = f"Меры поддержки. {service_name}. {subservice_name}",
            viber_id = user_id,
            keyboard = response_keyboard,
        )
    else:
        logging.info(f'[SUBSERVICE REQUEST] ERROR WHILE SENDING LINKS OF {subservice_name} SUBSERVICE')