from .views import UrlShortFormGenerator
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', UrlShortFormGenerator.as_view(), name='urlgenerator'),
]