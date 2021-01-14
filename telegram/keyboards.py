import logging

BASE_URL = 'https://xn--37-9kcqjffxnf3b.xn--p1ai/mery-gospodderzhki/'

MAIN_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Новости', 'callback_data': 'illuminator_NEWS'}],
        [{'text': 'Мероприятия', 'callback_data': 'illuminator_EVENTS'}],
        [{'text': 'Меры поддержки', 'callback_data': 'illuminator_SERVICES'}],
    ]
}

BACK_TO_MAIN_BUTTON = [{'text': 'Меню', 'callback_data': 'illuminator_BACK_MAIN'}]
BACK_TO_SERVICES_BUTTON = [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}]

def create_switch_keyboard(request_type, next_page = None, prev_page = None):
    inline_keyboard = []
    if next_page:
        inline_keyboard.append([{'text': 'Продолжение', 'callback_data': f'illuminator_{request_type}${next_page}'}])
    if prev_page:
        inline_keyboard.append([{'text': 'Назад', 'callback_data': f'illuminator_{request_type}${prev_page}'}])
    inline_keyboard.append(BACK_TO_MAIN_BUTTON)
    KEYBOARD = {
        'inline_keyboard': inline_keyboard
    }
    return KEYBOARD

def create_dynamic_service_keyboard(service_data):
    try:
        inline_keyboard = [
                [{'text': service.get('NAME'), 'callback_data': f"illuminator_SERVICE${service.get('ID')}"}] 
                for service in service_data
            ]
        inline_keyboard.append(BACK_TO_MAIN_BUTTON)
        return {'inline_keyboard': inline_keyboard}
    except Exception as e:
        logging.info(f'[DYNAMIC SERVICE KEYBOARD] CREATION ERROR')
        logging.info(f'{e}')
        return MAIN_KEYBOARD

def create_dynamic_subservice_keyboard(service_data, service_id):
    try:
        inline_keyboard = [
                [{'text': service.get('NAME'), 'callback_data': f'illuminator_SUBSERVICE${service.get("ID")}${service_id}'}] 
                for service in service_data
            ]
        inline_keyboard.append(BACK_TO_SERVICES_BUTTON)
        return {'inline_keyboard': inline_keyboard}
    except Exception as e:
        return MAIN_KEYBOARD

def create_dynamic_subservice_link_keyboard(service_data, service_id):
    try:
        inline_keyboard = [
                [{'text': service.get('NAME'), 'url': service.get('URL')}] 
                for service in service_data
            ]
        inline_keyboard.append([{'text': 'Назад', 'callback_data': f"illuminator_SERVICE${service_id}"}])
        return {'inline_keyboard': inline_keyboard}
    except Exception as e:
        return MAIN_KEYBOARD