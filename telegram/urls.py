from django.urls import path
from .views import entrypoint, send_message_to_users, test_send_message

urlpatterns = [
    path('', entrypoint),
    path('send', send_message_to_users),
    path('test', test_send_message),
]