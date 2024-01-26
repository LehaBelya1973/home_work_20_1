from django.urls import path

from mainapp.views import base

urlpatterns = [
    path('', base)
]