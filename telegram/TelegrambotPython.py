import requests
import json
import os
import logging

TOKEN = '1454168643:AAGQ8X7y9zWrSvsjZ5lYk6cKuwblTTwD55M' 
HOST_URL = 'https://5125b764b219.ngrok.io/telegram/'

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
