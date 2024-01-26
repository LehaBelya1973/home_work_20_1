from django.shortcuts import render

from mainapp.models import Product, Category


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Магазин - Главная',
    }
    return render(request, 'main/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории наших товаров:',
    }
    return render(request, 'main/categories.html', context)

