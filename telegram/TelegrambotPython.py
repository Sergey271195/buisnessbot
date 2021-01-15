import requests
import json
import os
import logging

TOKEN = os.environ.get("TELEGRAM_TOKEN")
HOST_URL = 'https://bot.xn--37-9kcqjffxnf3b.xn--p1ai/telegram/'
DEEPLINK_URL = 'https://t.me/MyBuisnessIvanovbot'

logging.basicConfig(filename='warning.log', encoding='utf-8', level=logging.WARNING)

class TelegramBot():
    
    def __init__(self):
        self.TOKEN = TOKEN
        self.BASE_URL = f'https://api.telegram.org/bot{self.TOKEN}'
        self.HOST_URL = HOST_URL
        self.HEADERS = {'Content-Type': 'application/json'}

    def create_webhook(self):
        logging.info('[TELEGRAM WEBHOOK] Setting telegram webhook'.upper())
        request_url = self.BASE_URL + '/setWebhook'
        json_data = json.dumps({'url': self.HOST_URL}, ensure_ascii = False)
        request = requests.post(request_url, headers = self.HEADERS, data = json_data)
        try:
            response = request.json()
            result = response.get('result')
            if result == True:
                logging.info('[TELEGRAM WEBHOOK] Telegram webhook was successfully created'.upper())
            else:
                logging.info('[TELEGRAM WEBHOOK] Telegram webhook was not set'.upper())
                logging.info(f'{response}')
            return response
        except Exception as e:
            logging.info('[TELEGRAM WEBHOOK] Wrong request parameters. Exception while processing TG response while setting webhook'.upper())
            logging.info(f'{request.text}')
            
            
    def remove_webhook(self):
        request_url = self.BASE_URL + '/deleteWebhook'
        request = requests.post(request_url)
        try:
            response = request.json()
            result = response.get('result')
            if result == True:
                logging.info('[TELEGRAM WEBHOOK] Telegram webhook was successfully deleted'.upper())
            else:
                logging.info('[TELEGRAM WEBHOOK] Telegram webhook was not successfully deleted'.upper())
                logging.info(f'{response}')
            return response
        except Exception as e:
            logging.info('[TELEGRAM WEBHOOK] Wrong request parameters. Exception while processing TG response while removing webhook'.upper())
            logging.info(f'{request.text}')
    
    def send_text_message_to_id(self, message, telegram_id, keyboard = False):
        logging.info(f'[TELEGRAM SEND MESSAGE] TRYING TO SEND MESSAGE TO USER WITH ID {telegram_id}')
        request_url = self.BASE_URL + '/sendMessage'
        data = {'chat_id': telegram_id, 'text': message, 'parse_mode': 'HTML'}
        if keyboard:
            data['reply_markup'] = keyboard
        json_data = json.dumps(data)
        try:
            request = requests.post(request_url, headers = self.HEADERS, data = json_data)
            response = request.json()
            if response.get('ok') == True:
                logging.info(f'[TELEGRAM SEND MESSAGE] SUCCESSFULLY SEND MESSAGE TO USER WITH ID {telegram_id}')
        except Exception as e:
            logging.info(f'[TELEGRAM SEND MESSAGE] EXCEPTION WHILE SENDING MESSAGE TO USER WITH ID {telegram_id}')
            logging.info(e)
            raise Exception(f'Exception while sending message to specified telegram_id {telegram_id}')

    
    def edit_text_message(self, message_id, message_update, user, keyboard = False):
        logging.info(f'[TELEGRAM EDIT MESSAGE] TRYING TO EDIT MESSAGE {message_id} TO telegram_user - {user.get("first_name")}')
        request_url = self.BASE_URL + '/editMessageText'
        data = {'chat_id': user.get("id"), 'message_id': message_id, 'text': message_update, 'parse_mode': 'HTML'}
        if keyboard:
            data['reply_markup'] = keyboard
        json_data = json.dumps(data)
        try:
            request = requests.post(request_url, headers = self.HEADERS, data = json_data)
            response = request.json()
            if response.get('ok') == True:
                logging.info(f'[TELEGRAM EDIT MESSAGE] SUCCESSFULLY EDIT MESSAGE {message_id} TO  telegram_user - {user.get("first_name")}')
            else:
                logging.info(f'[TELEGRAM EDIT MESSAGE] ERROR WHILE EDITING MESSAGE {message_id} TO  telegram_user - {user.get("first_name")}')
                logging.info(response)
        except Exception as e:
            logging.info(f'[TELEGRAM EDIT MESSAGE] EXCEPTION WHILE EDITING MESSAGE {message_id} TO  telegram_user - {user.get("first_name")}')
            logging.info(e)
