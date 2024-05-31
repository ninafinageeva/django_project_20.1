from django.conf import settings
from django.urls import path
from .apps import CatalogConfig
from catalog.views import product_list, product_detail
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]
