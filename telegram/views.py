from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import json
import logging

logging.basicConfig(level=logging.INFO)


@csrf_exempt
def entrypoint(request):
    logging.info("[TELEGRAM ENTRYPOINT]")
    try:
        request_body = json.loads(request.body)
        print(request_body)
        
    except Exception as e:
        logging.warning("[TELEGRAM ENTRYPOINT] ERROR WHILE RECIEVING REQUESTS TO ENTRYPOINT")
        logging.warning(e)

    return JsonResponse({'STATUS_CODE': 200})
