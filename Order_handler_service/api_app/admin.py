from django.contrib import admin

from .models import Order, OrderDish
from .models import Dish

admin.site.register(Order)
admin.site.register(OrderDish)
admin.site.register(Dish)