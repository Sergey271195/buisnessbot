from django.urls import path
from .views import create_webhook, entrypoint, remove_webhook

urlpatterns = [
    path('', entrypoint),
    path('webhook/set', create_webhook),
    path('webhook/remove', remove_webhook),
]