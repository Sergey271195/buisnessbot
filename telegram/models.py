from django.db import models

import logging 

logging.basicConfig(level=logging.INFO)

class TelegramUser(models.Model):

    telegram_id = models.IntegerField()
    bitrix_id = models.IntegerField(blank = True, null = True)
    name = models.CharField(max_length = 200)
    language_code = models.CharField(max_length = 20)

def check_or_create_user(request_user):

    logging.info("[CHECK OR CREATE USER]")
    try:
        telegram_user = TelegramUser.objects.get(telegram_id = request_user.get('id'))
        logging.info(f"[CHECK OR CREATE USER] USER ALREDAY EXISTS")
        logging.info(f"{telegram_user.__dict__}")
        return telegram_user
    except TelegramUser.DoesNotExist:
        try:
            new_user = TelegramUser(
                telegram_id = request_user.get('id'),
                name = request_user.get('first_name'),
                language_code = request_user.get('language_code'),
            )
            new_user.save()
            logging.info(f"[CHECK OR CREATE USER] NEW USER")
            logging.info(f"{new_user.__dict__}")
            return new_user
        except Exception as e:
            logging.info(f"[CHECK OR CREATE USER] EXCEPTION WHILE CREATING NEW USER")
            logging.info(f"{e}")
            return None

def check_or_create_user_with_context(request_user, bitrix_id):

    logging.info("[CHECK OR CREATE USER WITH CONTEXT]")
    logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] CREATING USER WITH BITRIX_ID = {bitrix_id}")
    if bitrix_id:
        try:
            telegram_user = TelegramUser.objects.get(telegram_id = request_user.get('id'), bitrix_id = bitrix_id)
            logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] USER ALREDAY EXISTS")
            logging.info(f"{telegram_user.__dict__}")
            return telegram_user
        except TelegramUser.DoesNotExist:
            telegram_user = check_or_create_user(request_user = request_user)
            logging.info("[CHECK OR CREATE USER WITH CONTEXT] FETCHING OR CREATING USER WITHOUT CONTEXT")
            if telegram_user:
                telegram_user.bitrix_id = bitrix_id
                telegram_user.save()
                logging.info(f"[CHECK OR CREATE USER WITH CONTEXT] ADDING BITRIX_ID = {bitrix_id} TO EXISTING USER")
                return telegram_user
            return telegram_user          
    else:
        logging.info("[CHECK OR CREATE USER WITH CONTEXT] SWITCHING TO CHECK OR CREATE USER WITHOUT CONTEXT")
        return check_or_create_user(request_user = request_user)
