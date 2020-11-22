BASE_URL = 'https://xn--37-9kcqjffxnf3b.xn--p1ai/mery-gospodderzhki/'

MAIN_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Новости', 'callback_data': 'illuminator_NEWS'}],
        [{'text': 'Мероприятия', 'callback_data': 'illuminator_EVENTS'}],
        [{'text': 'Меры поддержки', 'callback_data': 'illuminator_SERVICES'}],
    ]
}

SERVICES_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Продвижение', 'callback_data': 'illuminator_PROMOTION'}],
        [{'text': 'Производительность труда', 'callback_data': 'illuminator_PERFOMANCE'}],
        [{'text': 'Техприсоединение', 'callback_data': 'illuminator_TECH_CONNECTION'}],
        [{'text': 'Финансовая поддержка', 'callback_data': 'illuminator_FINANCIAL_SUPPORT'}],
        [{'text': 'Сельское хозяйство', 'callback_data': 'illuminator_AGRICULTURE'}],
        [{'text': 'Экспорт', 'callback_data': 'illuminator_EXPORT'}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_MAIN'}],
    ]
}

PROMOTION_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Консультации', 'url': f"{BASE_URL}prodvizhenie/"}],
        [{'text': 'Обучение', 'url': f"{BASE_URL}prodvizhenie/"}],
        [{'text': 'Продвижение', 'url': f"{BASE_URL}prodvizhenie/"}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}],
    ]
}

PERFOMANCE_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Повышение производительности труда', 'url': f"{BASE_URL}proizvoditelnost-truda/"}],
        [{'text': 'Инжиниринговые услуги', 'url': f"{BASE_URL}proizvoditelnost-truda/"}],
        [{'text': 'Национальные проекты', 'url': f"{BASE_URL}proizvoditelnost-truda/"}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}],
    ]
}

TECH_SUPPORT_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Консультации', 'url': f"{BASE_URL}tekhprisoedinenie/"}],
        [{'text': 'Организация первиочной заявки', 'url': f"{BASE_URL}tekhprisoedinenie/"}],
        [{'text': 'Анализ и обоснованность затрат', 'url': f"{BASE_URL}tekhprisoedinenie/"}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}],
    ]
}

FINANCIAL_SUPPORT_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Микрозаймы. Кредитование', 'url': f"{BASE_URL}finansovaya-podderzhka/"}],
        [{'text': 'Поручительство', 'url': f"{BASE_URL}finansovaya-podderzhka/"}],
        [{'text': 'Льготный лизинг', 'url': f"{BASE_URL}finansovaya-podderzhka/"}],
        [{'text': 'Займы специализированных фондов', 'url': f"{BASE_URL}finansovaya-podderzhka/"}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}],
    ]
}

AGRICULTURE_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Консультации и обучение', 'url': f"{BASE_URL}selskoe-khozyaystvo/"}],
        [{'text': 'Сопровождение с/х товаропроизводителей', 'url': f"{BASE_URL}selskoe-khozyaystvo/"}],
        [{'text': 'Меры господдержки с/х товаропроизводителей', 'url': f"{BASE_URL}selskoe-khozyaystvo/"}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}],
    ]
}

EXPORT_KEYBOARD = {
    'inline_keyboard': [
        [{'text': 'Консультации и обучение', 'url': f"{BASE_URL}eksport/"}],
        [{'text': 'Продвижение на экспорт', 'url': f"{BASE_URL}eksport/"}],
        [{'text': 'Перевод на иностранные языки', 'url': f"{BASE_URL}eksport/"}],
        [{'text': 'Поиск иностранных партнеров', 'url': f"{BASE_URL}eksport/"}],
        [{'text': 'Назад', 'callback_data': 'illuminator_BACK_SERVICES'}],
    ]
}