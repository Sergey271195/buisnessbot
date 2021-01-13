from django.db import models
import requests
import logging

logging.basicConfig(level=logging.INFO)
BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai/api/bot/setViberId.php"

class ViberUser(models.Model):

    viber_id = models.CharField(max_length = 100, unique = True)
    bitrix_id = models.IntegerField(blank = True, null = True)
    name = models.CharField(max_length = 200)
    language = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    subscribed = models.BooleanField(default = True, blank = True, null = True)

def check_or_create_user(request_user):

    logging.info("[CHECK OR CREATE USER]")
    try:
        viber_user = ViberUser.objects.get(viber_id = request_user.get('id'))
        logging.info(f"[CHECK OR CREATE USER] USER ALREDAY EXISTS")
        logging.info(f"{viber_user.__dict__}")
        return viber_user
    except ViberUser.DoesNotExist:
        try:
            new_user = ViberUser(
                viber_id = request_user.get('id'),
                name = request_user.get('name'),
                language = request_user.get('language'),
                country = request_user.get('country'),
            )
            new_user.save()
            logging.info(f"[CHECK OR CREATE USER] NEW USER")
            logging.info(f"{new_user.__dict__}")
            return new_user
        except Exception as e:
            logging.info(f"[CHECK OR CREATE USER] EXCEPTION WHILE CREATING NEW USER")
            logging.info(f"{e}")
            return None

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

        try:
            viber_user = ViberUser.objects.get(viber_id = request_user.get('id'), bitrix_id = bitrix_id)
            logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] USER ALREDAY EXISTS")
            logging.info(f"{viber_user.__dict__}")
            return viber_user
        except ViberUser.DoesNotExist:
            viber_user = check_or_create_user(request_user = request_user)
            logging.info("[CHECK OR CREATE USER WITH CONTEXT] FETCHING OR CREATING USER WITHOUT CONTEXT")
            if viber_user:
                viber_user.bitrix_id = bitrix_id
                viber_user.save()
                logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] ADDING BITRIX_ID = {bitrix_id} TO EXISTING USER")
                return viber_user
            return viber_user          
    else:
        logging.info("[CHECK OR CREATE USER WITH CONTEXT] SWITCHING TO CHECK OR CREATE USER WITHOUT CONTEXT")
        return check_or_create_user(request_user = request_user)