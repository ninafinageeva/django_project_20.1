
from django.contrib import admin
from django.urls import path

from .apps import CatalogConfig
from .views import index, contacts

app_name = CatalogConfig.name
urlpatterns = (
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')
)