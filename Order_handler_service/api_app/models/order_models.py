from django.db import models


class Order(models.Model):
    ORDER_STATUS = (
        ('waiting', 'В ожидании'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнен'),
        ('canceled', 'Отменен')
    )

    user_id = models.IntegerField()
    status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS,
        default='waiting'
    )
    special_requests = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # оно само будет обновляться при изменении записи

    def __str__(self):
        return f'Заказ номер {self.id}'


class OrderDish(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    dish_id = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.order} - {self.dish_id}'
