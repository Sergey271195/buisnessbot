from django.urls import path
from .views import create_webhook, entrypoint, remove_webhook, send_text_message, test_send_message

urlpatterns = [
    path('', entrypoint),
    path('viber/send', send_text_message),
    path('viber/test', test_send_message),
    path('webhook/set', create_webhook),
    path('webhook/remove', remove_webhook),
]