from django.urls import path
from .views import entrypoint, send_message_to_users

urlpatterns = [
    path('', entrypoint),
    path('send', send_message_to_users),
]