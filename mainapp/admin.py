from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, ProductCategory

admin.site.register(ProductCategory)
admin.site.register(Product)
