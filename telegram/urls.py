from django.urls import path
from .views import entrypoint

urlpatterns = [
    path('', entrypoint),
]