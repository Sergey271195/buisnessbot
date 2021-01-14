
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
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_NEWS",
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
        "ActionBody": "illuminator_EVENTS",
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
        "ActionBody": "illuminator_SERVICES",
        "Text": "Меры поддержки",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}

def create_dynamic_service_keyboard(service_data):
    try:
        buttons = [{
                    "Columns": 6,
                    "Rows": 1,
                    "ActionType": "reply",
                    "ActionBody": f"illuminator_SERVICE${service.get('ID')}",
                    "Text": service.get("NAME"),
                    "TextVAlign": "middle",
                    "TextHAlign": "center",
                    "TextOpacity": 60,
                    "TextSize": "regular"
                } for service in service_data]
        buttons.append(BACK_TO_MAIN_BUTTON)
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

SERVICES_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_PROMOTION",
        "Text": "Продвижение",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_PERFOMANCE",
        "Text": "Производительность труда",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_TECH_CONNECTION",
        "Text": "Техприсоединение",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_FINANCIAL_SUPPORT",
        "Text": "Финансовая поддержка",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_AGRICULTURE",
        "Text": "Сельское хозяйство",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_EXPORT",
        "Text": "Экспорт",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_MAIN",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}


PROMOTION_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}prodvizhenie/",
        "Text": "Консультации",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}prodvizhenie/",
        "Text": "Обучение",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}prodvizhenie/",
        "Text": "Продвижение",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_SERVICES",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}

PERFOMANCE_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}proizvoditelnost-truda/",
        "Text": "Повышение производительности труда",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}proizvoditelnost-truda/",
        "Text": "Инжиниринговые услуги",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}proizvoditelnost-truda/",
        "Text": "Национальные проекты",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_SERVICES",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}

TECH_SUPPORT_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}tekhprisoedinenie/",
        "Text": "Консультации",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}tekhprisoedinenie/",
        "Text": "Организация первиочной заявки",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}tekhprisoedinenie/",
        "Text": "Анализ и обоснованность затрат",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_SERVICES",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}


FINANCIAL_SUPPORT_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}finansovaya-podderzhka/",
        "Text": "Микрозаймы. Кредитование",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}finansovaya-podderzhka/",
        "Text": "Поручительство",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}finansovaya-podderzhka/",
        "Text": "Льготный лизинг",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}finansovaya-podderzhka/",
        "Text": "Займы специализированных фондов",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_SERVICES",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}

AGRICULTURE_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}selskoe-khozyaystvo/",
        "Text": "Консультации и обучение",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}selskoe-khozyaystvo/",
        "Text": "Сопровождение с/х товаропроизводителей",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}selskoe-khozyaystvo/",
        "Text": "Меры господдержки с/х товаропроизводителей",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_SERVICES",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}

EXPORT_KEYBOARD = {
    "Type":"keyboard",
    "DefaultHeight": True,
    "Buttons": [{
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}eksport/",
        "Text": "Консультации и обучение",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}eksport/",
        "Text": "Продвижение на экспорт",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}eksport/",
        "Text": "Перевод на иностранные языки",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "open-url",
        "ActionBody": f"{BASE_URL}eksport/",
        "Text": "Поиск иностранных партнеров",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    },
    {
        "Columns": 6,
        "Rows": 1,
        "ActionType": "reply",
        "ActionBody": "illuminator_BACK_SERVICES",
        "Text": "Назад",
        "TextVAlign": "middle",
        "TextHAlign": "center",
        "TextOpacity": 60,
        "TextSize": "regular"
    }]
}