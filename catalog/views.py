from django.shortcuts import render, get_object_or_404
from catalog.models import Product


# контроллеры для сайта

def product_list(request):
    """Выводит список товаров на сайте"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


