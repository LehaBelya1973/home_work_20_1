from django.db import models
from django.utils import timezone


NULLABLE = {'blank': True, 'null': True}


class Category:
    name_category =
    description_category =
    pass
    pass


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='Изображение', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey(Category, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    date_of_production = models.DateField(auto_now_add=True, verbose_name='Дата внесения товара', **NULLABLE)
    date_last_changes = models.DateField(auto_now=True, verbose_name='Дата последнего изменения', **NULLABLE)


