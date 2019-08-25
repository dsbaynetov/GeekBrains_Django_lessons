from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket


# Create your views here.
def main(request):
    content = {'title': 'Главная', }
    return render(request, 'mainapp/index.html', context=content)


# def products(request):
#     categories = ProductCategory.objects.all()
#     item_products = Product.objects.all()[:10]
#     content = {'title': 'Каталог', 'products': item_products, 'categories': categories }
#     return render(request, 'mainapp/products.html', context=content)

def products(request, pk=None):
    print(f"pk={pk}")
    title = 'Каталог'


    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        categories = get_object_or_404(ProductCategory, pk=pk)
        products_list = Product.objects.filter(category__pk=pk)
    else:
        categories = ProductCategory.objects.all()
        products_list = Product.objects.all()

    content = {'title': title, 'categories': categories,'products': products_list,'basket':basket}
    return render(request, 'mainapp/products.html', context=content)


def contacts(request):
    content = {'title': 'Контакты', }
    return render(request, 'mainapp/contacts.html', context=content)
