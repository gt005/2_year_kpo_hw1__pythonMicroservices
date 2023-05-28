from django.contrib import admin

from .models import Order, OrderDish
from .models import Dish


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'get_status_display', 'special_requests', 'created_at', 'updated_at')

    def get_status_display(self, obj):
        return obj.get_status_display()
    get_status_display.short_description = 'Статус'


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDish)
admin.site.register(Dish)