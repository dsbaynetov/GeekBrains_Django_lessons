from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.
def main(request):
    content = {'title': 'Главная', }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    categories = ProductCategory.objects.all()
    item_products = Product.objects.all()[:10]
    content = {'title': 'Каталог', 'products': item_products, 'categories': categories }
    return render(request, 'mainapp/products.html', context=content)


def contacts(request):
    content = {'title': 'Контакты', }
    return render(request, 'mainapp/contacts.html', context=content)
