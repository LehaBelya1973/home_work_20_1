from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import index, categories

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
]