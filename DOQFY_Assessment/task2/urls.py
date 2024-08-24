from .views import CreateContentTemplate, ViewSnippetContent
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', CreateContentTemplate.as_view(), name='createContent'),
    path('snippet/<slug:slug>/', ViewSnippetContent.as_view(),name='view_snippet')
]