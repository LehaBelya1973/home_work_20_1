from django.shortcuts import render

from mainapp.models import Product, Category


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'category_list': Category.objects.all(),
        'title': 'Магазин - Главная',
    }
    return render(request, 'main/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории наших товаров:',
    }
    return render(request, 'main/categories.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары из категории {category_item.name}',                             
    }
    return render(request, 'main/products.html', context)
