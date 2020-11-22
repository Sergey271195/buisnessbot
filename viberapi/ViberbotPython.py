import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = '4c783b57e380086b-c90dda0abe0e8ebe-7a99acd0bb05c2de'
HOST_URL = 'https://5125b764b219.ngrok.io'

KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "NEWS",
        "Text": "Новости",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "EVENTS",
        "Text": "Мероприятия",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "SERVICES",
        "Text": "Услуги",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}

class ViberBot():

    def __init__(self):
        self.TOKEN = TOKEN
        self.HEADERS = {'X-Viber-Auth-Token': self.TOKEN}
        self.HOST_URL = HOST_URL
        self.RESOURCE_WEBHOOK_URL = 'https://chatapi.viber.com/pa/set_webhook'
        self.RESOURCE_MESSAGE_URL = 'https://chatapi.viber.com/pa/send_message'
        self.RESOURCE_BROADCAST_URL = 'https://chatapi.viber.com/pa/broadcast_message'
        self.KEYBOARD = KEYBOARD

    def check_response_status(self, response):
        status = response.get('status')
        status_message = response.get('status_message')
        if status == 0 and status_message == 'ok':
            return 200
        return 400
    
    def create_webhook(self):
        logging.info("[CREATE WEBHOOK]")
        json_data = json.dumps({'url': self.HOST_URL}, ensure_ascii = False)
        request = requests.post(url = self.RESOURCE_WEBHOOK_URL, headers = self.HEADERS, data = json_data)
        if request.status_code == 200:
            response = request.json()
            response_status = self.check_response_status(response)
            
            if response_status == 200:
                logging.info("[CREATE WEBHOOK] SUCCESSFULLY CREATED WEBHOOK")
                return {'STATUS_CODE': 200}

            logging.info("[CREATE WEBHOOK] ERROR WHILE CREATING WEBHOOK")
            logging.info(f"[CREATE WEBHOOK] {response}")  

        return {'STATUS_CODE': 400}

    def remove_webhook(self):
        logging.info("[REMOVE WEBHOOK]")
        json_data = json.dumps({'url': ''}, ensure_ascii = False)
        request = requests.post(url = self.RESOURCE_WEBHOOK_URL, headers = self.HEADERS, data = json_data)
        response = request.json()
        logging.info("[REMOVE WEBHOOK] SUCCESSFULLY REMOVED WEBHOOK")
        return {'STATUS_CODE': 200}

    
    def send_text_message(self, message, receiver = None, keyboard = False):

        logging.info("[SEND MESSAGE]")

        post_data = {
            'sender': {
                'name': 'Viber Bot',
            },
            "type": 'text',
            "text": message,
        }

        if receiver:
            post_data['receiver'] = receiver.viber_id
        if keyboard:
            post_data['keyboard'] = self.KEYBOARD

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
                logging.info(f"[SEND MESSAGE] SUCCESSFULLY SEND TEXT MESSAGE {message}")
                return {'STATUS_CODE': 200}

            logging.info("[SEND MESSAGE] ERROR WHILE SENDING MESSAGE")
            logging.info(f"[SEND MESSAGE] {response}")  

        return {'STATUS_CODE': 400}


    def broadcast_message(self, message, ids):

            logging.info("[BROADCAST MESSAGE]")

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
                    logging.info(f"[BROADCAST MESSAGE] SUCCESSFULLY BROADCASTING TEXT MESSAGE {message}")
                    return {'STATUS_CODE': 200}

                logging.info("[BROADCAST MESSAGE] ERROR WHILE BROADCASTING MESSAGE")
                logging.info(f"[BROADCAST MESSAGE] {response}")  

            return {'STATUS_CODE': 400}