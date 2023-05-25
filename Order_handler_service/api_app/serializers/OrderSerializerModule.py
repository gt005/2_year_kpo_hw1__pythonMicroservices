from rest_framework import serializers

from ..models import OrderDish, Order


class OrderDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDish
        fields = ('dish_id', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format='%d %B %Y %H:%M:%S',
        required=False,
        read_only=True,
    )
    updated_at = serializers.DateTimeField(
        format='%d %B %Y %H:%M:%S',
        required=False,
        read_only=True,
    )
    orderdishes = OrderDishSerializer(source='orderdish_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('user_id', 'status', 'special_requests', 'created_at', 'updated_at', 'orderdishes')