from django.shortcuts import render
from django.http import JsonResponse

def entrypoint(request):
    return JsonResponse({'STATUS_CODE': 200})
