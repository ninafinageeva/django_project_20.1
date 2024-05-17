from django.urls import path

from .apps import CatalogConfig
from .views import index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index)
]