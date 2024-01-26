from django.shortcuts import render

from mainapp.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Магазин - наши товары:',
    }
    return render(request, 'main/index.html', context)

