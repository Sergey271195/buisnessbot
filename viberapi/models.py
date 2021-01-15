from django.db import models
import requests
import logging

logging.basicConfig(level=logging.INFO)
BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai/api/bot/setViberId.php"

def check_or_create_user_with_context(request_user, context):

    logging.info("[CHECK OR CREATE USER WITH CONTEXT]")
    bitrix_id, user_hash = None, None
    try:
        if 'userId'in context:
            user_info = context.replace('userId', '')
            bitrix_id, user_hash = user_info.split("_")
            logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] CREATING USER WITH BITRIX_ID = {bitrix_id}")
    except Exception as e:
        logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] WRONG CONTEXT PARAMETERS {context}")
    if bitrix_id and user_hash:

        db_url = f"{BASE_URL}?bitrix_id={bitrix_id}&viber_id={request_user.get('id')}&hash={user_hash}"
        logging.info(f"[SENDING NEW USER TO BASE URL VIBER] {db_url}")
        db_request = requests.get(db_url)
        logging.info(db_request.text)