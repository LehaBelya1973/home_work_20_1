from django.shortcuts import render

from mainapp.models import Category


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Магазин - категории товаров',
    }
    return render(request, 'main/index.html', context)

