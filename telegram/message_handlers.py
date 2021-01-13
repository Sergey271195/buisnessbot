from .TelegrambotPython import TelegramBot
from .keyboards import create_switch_keyboard

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


def handle_sub_service_request(user, message_id):
    pass
    

"""  result = response.get('result')
        is_more = response.get('isMore')
        request_page = re.search(re.compile(r'page=(?P<page_num>[0-9]+$)'), request_url)
        response_message = '\n\n'.join(
                [f'{num+1}. <a href="{BASE_URL}{entry.get("DETAIL_PAGE_URL")}">{entry.get("NAME")}</a>' 
                    for num, entry in enumerate(result)]
            )
        logging.info(f'[SERVICE REQUEST] SUCCESSFULLY HANDLED RESPONSE DATA') """