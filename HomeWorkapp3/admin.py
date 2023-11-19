from django.contrib import admin
from .models import User, Product, Order
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'price', 'quantity']


class UserAdmin(admin.ModelAdmin):
    """Список пользователей"""
    list_display = ['name', 'email', 'phone', 'address']


class OrderAdmin(admin.ModelAdmin):
    """Список Заказов"""
    list_display = ['customer', 'date_ordered', 'total_price']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
