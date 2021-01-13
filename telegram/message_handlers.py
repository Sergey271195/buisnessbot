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


def handle_news_request(user, message_id, page = None):
    next_page_num, prev_page_num = None, None
    logging.info('[NEWS REQUEST]')
    if page:
        logging.info(f'[NEWS REQUEST] REQUESTING PAGE {page}')
        request_url = f'{BASE_URL}/api/bot/getNews.php?count=5&page={page}'
    else:
        logging.info(f'[NEWS REQUEST] REQUESTING FIRST PAGE')
        request_url = f'{BASE_URL}/api/bot/getNews.php?count=5&page=1'
    request = requests.get(request_url)
    try:
        response = request.json()
        result = response.get('result')
        is_more = response.get('isMore')
        request_page = re.search(re.compile(r'page=(?P<page_num>[0-9]+$)'), request_url)
        response_message = '\n\n'.join(
                [f'{num+1}. <a href="{BASE_URL}{entry.get("DETAIL_PAGE_URL")}">{entry.get("NAME")}</a>' 
                    for num, entry in enumerate(result)]
            )
        logging.info(f'[NEWS REQUEST] SUCCESSFULLY HANDLED RESPONSE DATA')
        if request_page:
            try:
                curr_page_num = int(request_page.group('page_num'))
                if request_page != 1:
                    prev_page_num = curr_page_num - 1
                if is_more:
                    next_page_num = curr_page_num + 1
                response_keybaord = create_switch_keyboard(
                        request_type = 'NEWS',
                        next_page = next_page_num,
                        prev_page = prev_page_num
                    )
                if not page:
                    logging.info(f'[NEWS REQUEST] SUCCESSFULLY SENDING FISRT PAGE RESPONSE')
                    TELEGRAM_BOT.send_text_message(
                        message = response_message,
                        user = user,
                        keyboard = response_keybaord,
                    )
                else:
                    logging.info(f'[NEWS REQUEST] SUCCESSFULLY SENDING {page} PAGE RESPONSE')
                    TELEGRAM_BOT.edit_text_message(
                        message_update = response_message,
                        user = user,
                        keyboard = response_keybaord,
                        message_id = message_id,
                    )

            except Exception as e:
                logging.info(f'[NEWS REQUEST] EXCEPTION WHILE CREATING RESPONSE REQUEST')
                logging.info(f'{e}')

    except Exception as e:
        logging.info(f'[NEWS REQUEST] EXCEPTION WHILE HANDLING RESPONSE DATA')
        logging.info(f'{e}')


def handle_events_request(user, message_id, page = None):
    next_page_num, prev_page_num = None, None
    logging.info('[EVENTS REQUEST]')
    if page:
        logging.info(f'[EVENTS REQUEST] REQUESTING PAGE {page}')
        request_url = f'{BASE_URL}/api/bot/getEvents.php?count=5&page={page}'
    else:
        logging.info(f'[EVENTS REQUEST] REQUESTING FIRST PAGE')
        request_url = f'{BASE_URL}/api/bot/getEvents.php?count=5&page=1'
    request = requests.get(request_url)
    try:
        response = request.json()
        result = response.get('result')
        is_more = response.get('isMore')
        request_page = re.search(re.compile(r'page=(?P<page_num>[0-9]+$)'), request_url)
        response_message = '\n\n'.join(
                [f'{num+1}. <a href="{BASE_URL}{entry.get("DETAIL_PAGE_URL")}">{entry.get("NAME")}</a>' 
                    for num, entry in enumerate(result)]
            )
        logging.info(f'[EVENTS REQUEST] SUCCESSFULLY HANDLED RESPONSE DATA')
        if request_page:
            try:
                curr_page_num = int(request_page.group('page_num'))
                if request_page != 1:
                    prev_page_num = curr_page_num - 1
                if is_more:
                    next_page_num = curr_page_num + 1
                response_keybaord = create_switch_keyboard(
                        request_type = 'EVENTS',
                        next_page = next_page_num,
                        prev_page = prev_page_num
                    )
                if not page:
                    logging.info(f'[EVENTS REQUEST] SUCCESSFULLY SENDING FISRT PAGE RESPONSE')
                    TELEGRAM_BOT.send_text_message(
                        message = response_message,
                        user = user,
                        keyboard = response_keybaord,
                    )
                else:
                    logging.info(f'[EVENTS REQUEST] SUCCESSFULLY SENDING {page} PAGE RESPONSE')
                    TELEGRAM_BOT.edit_text_message(
                        message_update = response_message,
                        user = user,
                        keyboard = response_keybaord,
                        message_id = message_id,
                    )

            except Exception as e:
                logging.info(f'[EVENTS REQUEST] EXCEPTION WHILE CREATING RESPONSE REQUEST')
                logging.info(f'{e}')

    except Exception as e:
        logging.info(f'[EVENTS REQUEST] EXCEPTION WHILE HANDLING RESPONSE DATA')
        logging.info(f'{e}')


def handle_services_request(user, message_id, service = None):
    next_page_num, prev_page_num = None, None
    logging.info('[SERVICE REQUEST]')
    if service:
        logging.info(f'[SERVICE REQUEST] REQUESTING SERVICE {service}')
        request_url = f'{BASE_URL}/api/bot/getServices.php?section={service}'
    else:
        logging.info(f'[SERVICE REQUEST] REQUESTING SERVICES LIST')
        request_url = f'{BASE_URL}/api/bot/getServices.php'
    request = requests.get(request_url)
    try:
        print(request.text)
        response = request.json()
        print(response)
       
    except Exception as e:
        logging.info(f'[SERVICE REQUEST] EXCEPTION WHILE CREATING RESPONSE REQUEST')
        logging.info(f'{e}')


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
    

"""  result = response.get('result')
        is_more = response.get('isMore')
        request_page = re.search(re.compile(r'page=(?P<page_num>[0-9]+$)'), request_url)
        response_message = '\n\n'.join(
                [f'{num+1}. <a href="{BASE_URL}{entry.get("DETAIL_PAGE_URL")}">{entry.get("NAME")}</a>' 
                    for num, entry in enumerate(result)]
            )
        logging.info(f'[SERVICE REQUEST] SUCCESSFULLY HANDLED RESPONSE DATA') """