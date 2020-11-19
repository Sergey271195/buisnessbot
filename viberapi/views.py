from django.shortcuts import render
from django.http import JsonResponse

def create_webhook(request):
    print(request.method)
    return JsonResponse({'STATUS_CODE': 200})
