from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import BasketSlot


# Create your views here.
def main(request):
    content = {'title': 'Главная', }
    return render(request, 'mainapp/index.html', context=content)


def get_basket(user):
    if user.is_authenticated:
        return BasketSlot.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    products = Product.objects.filter(is_hot=True).first()
    return products

def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products

def products(request, pk=None):
    #    print(f"pk={pk}")
    title = 'Каталог'
    basket = get_basket(request.user)
    categories = ProductCategory.objects.all()
    if pk:
        #        categories = get_object_or_404(ProductCategory, pk=pk)
        products_list = Product.objects.filter(category__pk=pk)
    else:
        products_list = Product.objects.all()

    hot_product = get_hot_product()

    content = {'title': title, 'hot_product': hot_product, 'categories': categories, 'products': products_list, 'basket': basket}
    return render(request, 'mainapp/products.html', context=content)


def product(request, pk):
    title = 'продукты'
    content = {
        'title': title,
        'categories': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', content)


def contacts(request):
    content = {'title': 'Контакты', }
    return render(request, 'mainapp/contacts.html', context=content)
