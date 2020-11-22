import requests
import json

TOKEN = '1454168643:AAGQ8X7y9zWrSvsjZ5lYk6cKuwblTTwD55M' 
HOST_URL = 'https://5125b764b219.ngrok.io/telegram'


class TelegramBot():
    
    def __init__(self):
        self.TOKEN = TOKEN
        self.BASE_URL = f'https://api.telegram.org/bot{self.TOKEN}'
    
    def set_webhook(self):
        pass
