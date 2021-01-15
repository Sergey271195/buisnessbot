import requests
import json
import logging

from .keyboards import MAIN_KEYBOARD

logging.basicConfig(level=logging.INFO)

TOKEN = '4c783b57e380086b-c90dda0abe0e8ebe-7a99acd0bb05c2de'
#HOST_URL = 'https://8c2cfc83235d.ngrok.io'
HOST_URL = 'https://bot.xn--37-9kcqjffxnf3b.xn--p1ai/'
DEEPLINK_URL = 'viber://pa?chatUri=testwebpythonbot'

class ViberBot():

    def __init__(self):
        self.TOKEN = TOKEN
        self.HEADERS = {'X-Viber-Auth-Token': self.TOKEN}
        self.HOST_URL = HOST_URL
        self.RESOURCE_WEBHOOK_URL = 'https://chatapi.viber.com/pa/set_webhook'
        self.RESOURCE_MESSAGE_URL = 'https://chatapi.viber.com/pa/send_message'
        self.RESOURCE_BROADCAST_URL = 'https://chatapi.viber.com/pa/broadcast_message'

    def check_response_status(self, response):
        status = response.get('status')
        status_message = response.get('status_message')
        if status == 0 and status_message == 'ok':
            return 200
        return 400
    
    def create_webhook(self):
        logging.info("[VIBER WEBHOOK] CREATING WEBHOOK")
        json_data = json.dumps({'url': self.HOST_URL}, ensure_ascii = False)
        request = requests.post(url = self.RESOURCE_WEBHOOK_URL, headers = self.HEADERS, data = json_data)
        if request.status_code == 200:
            response = request.json()
            response_status = self.check_response_status(response)
            
            if response_status == 200:
                logging.info("[VIBER WEBHOOK] SUCCESSFULLY CREATED WEBHOOK")
                return {'STATUS_CODE': 200}

            logging.info("[VIBER WEBHOOK] ERROR WHILE CREATING WEBHOOK")
            logging.info(f"[VIBER WEBHOOK] {response}")  

        return {'STATUS_CODE': 400}

    def remove_webhook(self):
        logging.info("[VIBER WEBHOOK] REMOVING WEBHOOK")
        json_data = json.dumps({'url': ''}, ensure_ascii = False)
        request = requests.post(url = self.RESOURCE_WEBHOOK_URL, headers = self.HEADERS, data = json_data)
        response = request.json()
        logging.info("[VIBER WEBHOOK] SUCCESSFULLY REMOVED WEBHOOK")
        return {'STATUS_CODE': 200}


    def send_rich_media(self, media, viber_id = None, keyboard = False):
        logging.info("[SEND RICH MEDIA VIBER] SENDING MESSAGE")

        post_data = {
            'sender': {
                'name': 'Viber Bot',
            },
            "type":"rich_media",
            "min_api_version": 7,
            "rich_media": media,
        }

        if viber_id:
            post_data['receiver'] = viber_id
        if keyboard:
            post_data['keyboard'] = keyboard

        json_data = json.dumps(post_data, ensure_ascii = False)

        request = requests.post(
            url = self.RESOURCE_MESSAGE_URL,
            headers = self.HEADERS,
            data = json_data.encode('utf-8'),
        )
        
        if request.status_code == 200:
            response = request.json()
            response_status = self.check_response_status(response)
            
            if response_status == 200:
                logging.info(f"[SEND MESSAGE VIBER] SUCCESSFULLY SEND TEXT MESSAGE {media}")
                return {'STATUS_CODE': 200}

            logging.info("[SEND MESSAGE VIBER] ERROR WHILE SENDING MESSAGE")
            logging.info(f"[SEND MESSAGE VIBER] {response}")  

        return {'STATUS_CODE': 400}
    
    def send_text_message(self, message, viber_id = None, keyboard = False):

        logging.info("[SEND MESSAGE VIBER] SENDING MESSAGE")

        post_data = {
            'sender': {
                'name': 'Viber Bot',
            },
            "type": 'text',
            "text": message,
        }

        if viber_id:
            post_data['receiver'] = viber_id
        if keyboard:
            post_data['keyboard'] = keyboard

        json_data = json.dumps(post_data, ensure_ascii = False)

        request = requests.post(
            url = self.RESOURCE_MESSAGE_URL,
            headers = self.HEADERS,
            data = json_data.encode('utf-8'),
        )
        
        if request.status_code == 200:
            response = request.json()
            response_status = self.check_response_status(response)
            
            if response_status == 200:
                logging.info(f"[SEND MESSAGE VIBER] SUCCESSFULLY SEND TEXT MESSAGE {message}")
                return {'STATUS_CODE': 200}

            logging.info("[SEND MESSAGE VIBER] ERROR WHILE SENDING MESSAGE")
            logging.info(f"[SEND MESSAGE VIBER] {response}")  

        return {'STATUS_CODE': 400}


    def broadcast_message(self, message, ids):

            logging.info("[BROADCAST MESSAGE VIBER]")

            post_data = {
                'sender': {
                    'name': 'Viber Bot',
                },
                "type": 'text',
                "text": message,
                "broadcast_list": ids,
            }

            json_data = json.dumps(post_data, ensure_ascii = False)

            request = requests.post(
                url = self.RESOURCE_BROADCAST_URL,
                headers = self.HEADERS,
                data = json_data.encode('utf-8'),
            )
            
            if request.status_code == 200:
                response = request.json()
                response_status = self.check_response_status(response)
                
                if response_status == 200:
                    logging.info(f"[BROADCAST MESSAGE VIBER] SUCCESSFULLY BROADCASTING TEXT MESSAGE {message}")
                    return {'STATUS_CODE': 200}

                logging.info("[BROADCAST MESSAGE VIBER] ERROR WHILE BROADCASTING MESSAGE")
                logging.info(f"[BROADCAST MESSAGE VIBER] {response}")  
                raise Exception(f'[BROADCAST MESSAGE VIBER] ERROR WHILE BROADCASTING MESSAGE"')

            return {'STATUS_CODE': 400}