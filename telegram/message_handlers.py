from .TelegrambotPython import TelegramBot
from .keyboards import (create_switch_keyboard, create_dynamic_service_keyboard, 
                        create_dynamic_subservice_keyboard, create_dynamic_subservice_link_keyboard)

import requests
import re
import logging
import json

logging.basicConfig(level=logging.INFO)
TELEGRAM_BOT = TelegramBot()

BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai"

def get_json_data(url):
    try:
        request = requests.get(url)
        return request.json()
    except Exception as e:
        logging.info(f"[REQUEST EXCEPTION] {e}")

def prepare_paged_response(paged_data):
    if paged_data:
        return '\n\n'.join(
                [f'{num+1}. <a href="{BASE_URL}{entry.get("DETAIL_PAGE_URL")}">{entry.get("NAME")}</a>' 
                    for num, entry in enumerate(paged_data)]
            )

def prepare_paged_response_for_viber(paged_data):
    if paged_data:
        buttons = [
            {  
                "Columns": 6,
                "Rows": 5,
                "ActionType": "open-url",
                "ActionBody": f'{num+1}. {BASE_URL}{entry.get("DETAIL_PAGE_URL")}',
                "Text": entry.get("NAME"),
                "TextVAlign": "middle",
                "TextHAlign": "middle",
                "TextOpacity": 60,
                "TextSize": "regular"
            } for num, entry in enumerate(paged_data)
        ]
        media = {
        "Type":"rich_media",
        "ButtonsGroupColumns": 6,
        "ButtonsGroupRows": 5,
        "BgColor":"#FFFFFF",
        "Buttons": buttons
        }
        return media

def get_json_paged_data(url, request_page):
    response = get_json_data(url)
    try:
        paged_data = response.get('result')
        is_more = response.get('isMore')
        logging.info(f'[PAGED REQUEST] SUCCESSFULLY RETURNING PAGE {request_page} DATA')
        return [paged_data, is_more, None]
    except Exception as e:
        logging.info(f'[PAGED REQUEST] EXCEPTION WHILE PARSING PAGE {request_page} DATA')
        return [None, None, "Exception while parsing"]

def get_paged_data(url, request_page, default_message = None, viber = False):
    paged_data, is_more, exception = get_json_paged_data(url, request_page)
    if not exception:
        response_message = prepare_paged_response_for_viber(paged_data) if viber else prepare_paged_response(paged_data)
        if not response_message:
            response_message = default_message
        prev_page_num = request_page - 1 if request_page != 1 else None
        next_page_num = request_page + 1 if is_more else None
        return (response_message, prev_page_num, next_page_num)

def get_news_data_for_page(page = None, viber = False):
    
    request_page = page if page else 1
    logging.info(f'[NEWS REQUEST] REQUESTING PAGE {request_page}')
    request_url = f'{BASE_URL}/api/bot/getNews.php?count=5&page={request_page}'
    return get_paged_data(
            request_url, request_page, "В настоящее время актуальных новостей нет", viber
        )


def get_events_data_for_page(page = None, viber = False):
    
    request_page = page if page else 1
    logging.info(f'[EVENTS REQUEST] REQUESTING PAGE {request_page}')
    request_url = f'{BASE_URL}/api/bot/getEvents.php?count=5&page={request_page}'
    return get_paged_data(
            request_url, request_page, "В настоящее время никаких мероприятий не запланировано", viber
        )


def handle_news_request(user, message_id, page = None):

    response_message, prev_page_num, next_page_num = get_news_data_for_page(page)
    response_keyboard = create_switch_keyboard(
            request_type = 'NEWS',
            next_page = next_page_num,
            prev_page = prev_page_num
        )

    logging.info(f'[NEWS REQUEST] SUCCESSFULLY SENDING {page} PAGE RESPONSE')
    TELEGRAM_BOT.edit_text_message(
        message_update = response_message,
        user = user,
        keyboard = response_keyboard,
        message_id = message_id,
    )


def handle_events_request(user, message_id, page = None):
    response_message, prev_page_num, next_page_num = get_events_data_for_page(page)
    response_keyboard = create_switch_keyboard(
            request_type = 'EVENTS',
            next_page = next_page_num,
            prev_page = prev_page_num
        )
    logging.info(f'[EVENTS REQUEST] SUCCESSFULLY SENDING {page} PAGE RESPONSE')
    TELEGRAM_BOT.edit_text_message(
        message_update = response_message,
        user = user,
        keyboard = response_keyboard,
        message_id = message_id,
    )


def handle_service_list_request(user, message_id):
    logging.info('[SERVICE LIST REQUEST]')
    request_url = f'{BASE_URL}/api/bot/getServices.php'
    request = requests.get(request_url)
    try:
        response = request.json()
        response_keyboard = create_dynamic_service_keyboard(response)
        response_message = 'Доступные меры поддержки'
        logging.info(f'[SERVICE LIST REQUEST] SUCCESSFULLY SENDING LIST OF SERVICES')
        TELEGRAM_BOT.edit_text_message(
            message_update = response_message,
            user = user,
            keyboard = response_keyboard,
            message_id = message_id,
        )
       
    except Exception as e:
        logging.info(f'[SERVICE LIST REQUEST] EXCEPTION WHILE CREATING SERVICE LIST')
        logging.info(f'{e}')


def get_callback_data(callback_data):
    if "$" in callback_data:
        try:
            necessary_data = int(callback_data.split("$")[1])
            return necessary_data
        except Exception as e:
            return

def get_subservice_callback_data(callback_data):
    if "$" in callback_data:
        try:
            splitted_data = callback_data.split("$")
            subservice_id = int(splitted_data[1])
            service_id = int(splitted_data[2])
            return [subservice_id, service_id]
        except Exception as e:
            return

def request_service(url):
    logging.info(f"[REQUESTINQ URL] {url}")
    try:
        request = requests.get(url)
        response = request.json()
        logging.info(f"[REQUESTING URL] SUCCESFULLY RETURNING REQUESTED DATA")
        logging.info(response)
        return response
    except Exception as e:
        logging.info(f"[REQUESTING URL] EXCEPTION RETURNING REQUESTED DATA")
        logging.info(e)
        return

def get_service_name(url, service_id):
    try:
        service_list = request_service(url)
        service = list(filter(lambda x: int(x.get('ID')) == service_id, service_list))[0].get("NAME")
        return service
    except Exception as e:
        return ""

def handle_service_request(user, message_id, data):
    service_id = get_callback_data(data)
    service_name = get_service_name(f"{BASE_URL}/api/bot/getServices.php", service_id)
    service_data = request_service(f"{BASE_URL}/api/bot/getServices.php?section={service_id}")
    response_keyboard = create_dynamic_subservice_keyboard(service_data, service_id)
    if service_data:
        logging.info(f'[SERVICE REQUEST] SUCCESSFULLY SENDING SUBSERVICES OF {service_name} SERVICE')
        TELEGRAM_BOT.edit_text_message(
            message_update = "Меры поддержки. " + service_name,
            user = user,
            keyboard = response_keyboard,
            message_id = message_id,
        )
    else:
        logging.info(f'[SERVICE REQUEST] ERROR WHILE SENDING SUBSERVICES OF {service_name} SERVICE')


def handle_sub_service_request(user, message_id, data):
    subservice_id, service_id = get_subservice_callback_data(data)
    service_name = get_service_name(f"{BASE_URL}/api/bot/getServices.php", service_id)
    subservice_name = get_service_name(f"{BASE_URL}/api/bot/getServices.php?section={service_id}", subservice_id)
    subservice_data = request_service(f"{BASE_URL}/api/bot/getServices.php?subsection={subservice_id}")
    response_keyboard = create_dynamic_subservice_link_keyboard(subservice_data, service_id)
    if subservice_data:
        logging.info(f'[SUBSERVICE REQUEST] SUCCESSFULLY SENDING LINKS OF {subservice_name} SUBSERVICE')
        TELEGRAM_BOT.edit_text_message(
            message_update = f"Меры поддержки. {service_name}. {subservice_name}",
            user = user,
            keyboard = response_keyboard,
            message_id = message_id,
        )
    else:
        logging.info(f'[SUBSERVICE REQUEST] ERROR WHILE SENDING LINKS OF {subservice_name} SUBSERVICE')