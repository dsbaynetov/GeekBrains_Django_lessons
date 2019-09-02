from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, ProductCategory

admin.site.register(ProductCategory)

#добавляем поля для отображения
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'price', 'is_hot',)
    list_filter = ('is_hot',)
    search_fields = ('name','category__name')
