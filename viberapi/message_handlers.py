from .ViberbotPython import ViberBot
from .keyboards import (create_switch_keyboard, create_dynamic_service_keyboard, 
                        create_dynamic_subservice_keyboard, create_dynamic_subservice_link_keyboard)

import requests
import re
import logging
import json

logging.basicConfig(level=logging.INFO)
VIBER_BOT = ViberBot()

BASE_URL = "https://xn--37-9kcqjffxnf3b.xn--p1ai"

