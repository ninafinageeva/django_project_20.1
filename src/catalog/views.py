from django.shortcuts import render

from src.catalog.models import Product


# контроллеры для сайта

def product_list(request):
    """Выводит список товаров на сайте"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    product_pk = Product.objects.get(pk=pk)
    context = {'product': product_pk}
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    """Принимает контактные данные от пользователя с сайта"""
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')
    return render(request, 'catalog/contacts.html')