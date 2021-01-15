import logging
logging.basicConfig(filename='warning.log', encoding='utf-8', level=logging.WARNING)
BASE_URL = 'https://xn--37-9kcqjffxnf3b.xn--p1ai/mery-gospodderzhki/'

def create_standart_button(action_type, action_body, text):
    return {
                "Columns": 6,
                "Rows": 1,
                "ActionType": action_type,
                "ActionBody": action_body,
                "Text": text,
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            }

BACK_TO_SERVICES_BUTTON = create_standart_button(
        action_type = "reply", action_body = "illuminator_BACK_SERVICES", text = "Назад"
    )
BACK_TO_MAIN_BUTTON = create_standart_button(
        action_type = "reply", action_body = "illuminator_BACK_MAIN", text = "Меню"
    )

def create_switch_keyboard(request_type, next_page = None, prev_page = None):
    buttons = []
    if next_page:
        next_button = create_standart_button(
                action_type = "reply", action_body =  f'illuminator_{request_type}${next_page}', text = "Продолжение"
            )
        buttons.append(next_button)
    if prev_page:
        prev_button = create_standart_button(
                action_type = "reply", action_body =  f'illuminator_{request_type}${prev_page}', text = "Назад"
            )
        buttons.append(prev_button)
    buttons.append(BACK_TO_MAIN_BUTTON)
    KEYBOARD = {
        "Type":"keyboard",
        "DefaultHeight": True,
        "Buttons": buttons
    }
    return KEYBOARD



MAIN_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [
        create_standart_button(
            action_type = "reply", 
            action_body = f"illuminator_NEWS", 
            text = "Новости"
        ), 
        create_standart_button(
            action_type = "reply", 
            action_body = f"illuminator_EVENTS", 
            text = "Мероприятия"
        ), 
        create_standart_button(
            action_type = "reply", 
            action_body = f"illuminator_SERVICES", 
            text = "Меры поддержки"
        )]
}

def create_dynamic_service_keyboard(service_data):
    try:
        buttons = [create_standart_button(
                    action_type = "reply", 
                    action_body = f"illuminator_SERVICE${service.get('ID')}", 
                    text = service.get("NAME")
                ) for service in service_data]
        buttons.append(BACK_TO_MAIN_BUTTON)
        print(buttons)
        return {
                "Type":"keyboard",
                "DefaultHeight": True,
                "Buttons": buttons,
            }
    except Exception as e:
        logging.info(f'[DYNAMIC SERVICE KEYBOARD] CREATION ERROR ')
        logging.info(f'{e}')
        return MAIN_KEYBOARD

def create_dynamic_subservice_keyboard(service_data, service_id):
    try:
        buttons = [
            create_standart_button(
                    action_type = "reply", 
                    action_body = f'illuminator_SUBSERVICE${service.get("ID")}${service_id}', 
                    text = service.get("NAME")
                ) for service in service_data
            ]
        buttons.append(BACK_TO_SERVICES_BUTTON)
        return {
                "Type":"keyboard",
                "DefaultHeight": True,
                "Buttons": buttons,
            }
    except Exception as e:
        logging.info(f'[DYNAMIC SUBSERVICE KEYBOARD] CREATION ERROR ')
        logging.info(f'{e}')
        return MAIN_KEYBOARD

def create_dynamic_subservice_link_keyboard(service_data, service_id):
    try:
        buttons = [
            create_standart_button(
                    action_type = "open-url", 
                    action_body = service.get('URL'), 
                    text = service.get("NAME")
                ) for service in service_data
            ]
        buttons.append(create_standart_button(
                action_type = "reply", 
                action_body = f"illuminator_SERVICE${service_id}", 
                text = "Назад"
            ))
        return {
                "Type":"keyboard",
                "DefaultHeight": True,
                "Buttons": buttons,
            }
    except Exception as e:
        logging.info(f'[DYNAMIC SUBSERVICE KEYBOARD] CREATION ERROR ')
        logging.info(f'{e}')
        return MAIN_KEYBOARD
