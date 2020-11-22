from django.url import path
from .views import entrypoint

urlpatterns = [
    path('', entrypoint),
]