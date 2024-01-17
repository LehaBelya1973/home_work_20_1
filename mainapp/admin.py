from django.contrib import admin

from mainapp.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',
                    'product_category', 'price', 'date_of_production')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category', 'description_category')
