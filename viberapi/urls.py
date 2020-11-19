from django.urls import path
from .views import create_webhook

urlpatterns = [
    path('', create_webhook),
]