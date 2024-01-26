from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import index, categories, category_product

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/mainapp/', category_product, name='category_product'),
]