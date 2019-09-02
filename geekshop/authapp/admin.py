from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot

# Register your models here.
admin.site.register(ShopUser)

class BasketSlotInlibe(admin.TabularInline):
    model = BasketSlot
    fields = ('product','quantity',)
    extra = 0 #сколько показывать предзаполненных полей


class ShopUserWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True

@admin.register(ShopUserWithBasket)

class ShopUserWithBasketAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_basket_quantity', 'get_basket_cost')
    fields = ('username',)
    readonly_fields = ('username',)
    inlines = (BasketSlotInlibe,)

    #переороеделим для показа только пользователей у кого есть корзина
    def get_queryset(self, request):
        queryset = super(ShopUserWithBasketAdmin, self ).get_queryset(request)
        queryset = queryset.filter(basket__quantity__gt=0).distinct()
        return queryset

    #поля вычисляемые, отсутсвующие в таблицах
    def get_basket_quantity(self, instance):
        basket = instance.basket.all()
        total_quantity = sum(list(map(lambda basket_slot: basket_slot.total_quantity, basket)))
        return total_quantity

    def get_basket_cost(self, instance):
        basket = instance.basket.all()
        total_cost = sum(list(map(lambda basket_slot: basket_slot.total_cost, basket)))
        return total_cost

    get_basket_quantity.short_description = 'Товаров в корзине'
    get_basket_cost.short_description = 'Стоимость в корзине'