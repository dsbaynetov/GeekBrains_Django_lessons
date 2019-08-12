from django.shortcuts import render


# Create your views here.
def main(request):
    content = {'title': 'Главная', }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    item_products = [
        {'product':'Huawei Watch GT', 'image': '/static/img/watch-gt.jpg'},
        {'product':'Samsung Gear S3', 'image': '/static/img/gears3.jpg'},
    ]
    content = {'title': 'Каталог', 'products': item_products }
    return render(request, 'mainapp/products.html', context=content)


def contacts(request):
    content = {'title': 'Контакты', }
    return render(request, 'mainapp/contacts.html', context=content)
