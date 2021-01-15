from django.db import models

import requests
import logging 

logging.basicConfig(filename='warning.log', encoding='utf-8', level=logging.WARNING)
BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai/api/bot/setTelegramId.php"

def check_or_create_user_with_context(request_user, user_info):

    logging.info("[CHECK OR CREATE USER WITH CONTEXT]")
    logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] CREATING USER WITH USER INFO = {user_info}")

    bitrix_id, user_hash = None, None
    try:
        bitrix_id, user_hash = user_info.split("_")
        logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] CREATING USER WITH BITRIX_ID = {bitrix_id}")
    except Exception as e:
        logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] WRONG CONTEXT PARAMETERS {user_info}")

    if bitrix_id:
        db_url = f"{BASE_URL}?bitrix_id={bitrix_id}&telegram_id={request_user.get('id')}&hash={user_hash}"
        logging.info(f"[SENDING NEW USER TO BASE URL TELEGRAM] {db_url}")
        db_request = requests.get(db_url)
        logging.info(db_request.status_code)
