
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('viberapi.urls')),
    path('telegram/', include('telegram.urls')),
]
