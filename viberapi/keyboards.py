
BASE_URL = 'https://xn--37-9kcqjffxnf3b.xn--p1ai/mery-gospodderzhki/'


def create_switch_keyboard(request_type, next_page = None, prev_page = None):
    if next_page and prev_page:
        KEYBOARD = {
            "Type":"keyboard",
            "DefaultHeight": True,
            "Buttons": [{
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_{request_type}${next_page}',
                "Text": "Продолжение",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            },
            {
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_{request_type}${prev_page}',
                "Text": "Назад",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            },
            {
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_BACK_MAIN',
                "Text": "Меню",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            }]
        }
    elif next_page:
        KEYBOARD = {
            "Type":"keyboard",
            "DefaultHeight": True,
            "Buttons": [{
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_{request_type}${next_page}',
                "Text": "Продолжение",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            },
            {
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_BACK_MAIN',
                "Text": "Меню",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            }]
        }
    else:
        KEYBOARD = {
            "Type":"keyboard",
            "DefaultHeight": True,
            "Buttons": [{
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_{request_type}${prev_page}',
                "Text": "Назад",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            },
            {
                "Columns": 6,
                "Rows": 1,
                "ActionType": "reply",
                "ActionBody": f'illuminator_BACK_MAIN',
                "Text": "Меню",
                "TextVAlign": "middle",
                "TextHAlign": "center",
                "TextOpacity": 60,
                "TextSize": "regular"
            }]
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