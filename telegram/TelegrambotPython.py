import requests
import json
import os
import logging

TOKEN = '1454168643:AAGQ8X7y9zWrSvsjZ5lYk6cKuwblTTwD55M' 
HOST_URL = 'https://0c800ab0968a.ngrok.io/telegram/'
DEEPLINK_URL = 'https://t.me/MyBuisnessIvanovbot'

logging.basicConfig(level=logging.INFO)

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

    
    def send_text_message(self, message, user, keyboard = False):
        logging.info(f'[TELEGRAM SEND MESSAGE] TRYING TO SEND MESSAGE TO {user.name}-{user.telegram_id}')
        request_url = self.BASE_URL + '/sendMessage'
        data = {'chat_id': user.telegram_id, 'text': message, 'parse_mode': 'HTML'}
        if keyboard:
            data['reply_markup'] = keyboard
        json_data = json.dumps(data)
        try:
            request = requests.post(request_url, headers = self.HEADERS, data = json_data)
            response = request.json()
            if response.get('ok') == True:
                logging.info(f'[TELEGRAM SEND MESSAGE] SUCCESSFULLY SEND MESSAGE TO {user.name}-{user.telegram_id}')
        except Exception as e:
            logging.info(f'[TELEGRAM SEND MESSAGE] EXCEPTION WHILE SENDING MESSAGE TO {user.name}-{user.telegram_id}')
            logging.info(e)

    
    def edit_text_message(self, message_id, message_update, user, keyboard = False):
        logging.info(f'[TELEGRAM EDIT MESSAGE] TRYING TO EDIT MESSAGE {message_id} TO {user.name}-{user.telegram_id}')
        request_url = self.BASE_URL + '/editMessageText'
        data = {'chat_id': user.telegram_id, 'message_id': message_id, 'text': message_update, 'parse_mode': 'HTML'}
        if keyboard:
            data['reply_markup'] = keyboard
        json_data = json.dumps(data)
        try:
            request = requests.post(request_url, headers = self.HEADERS, data = json_data)
            response = request.json()
            if response.get('ok') == True:
                logging.info(f'[TELEGRAM EDIT MESSAGE] SUCCESSFULLY EDIT MESSAGE {message_id} TO {user.name}-{user.telegram_id}')
        except Exception as e:
            logging.info(f'[TELEGRAM EDIT MESSAGE] EXCEPTION WHILE EDITING MESSAGE {message_id} TO {user.name}-{user.telegram_id}')
            logging.info(e)
