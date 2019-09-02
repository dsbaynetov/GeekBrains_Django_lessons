from django.db import models
from django.conf import settings
from mainapp.models import Product


class BasketSlot(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity


    @property
    def total_quantity(self):
        "return total quantity for user"
        _items = BasketSlot.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        # print(_totalquantity)
        # print(f"_totalquantity={_totalquantity}")
        return _totalquantity


    @property
    def total_cost(self):
        "return total cost for user"
        _items = BasketSlot.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product_cost, _items)))
        return _totalcost

