from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Dish, Order
from ..serializers import DishSerializer, OrderSerializer


class ListAvailableToOrderDishes(APIView):
    """
    Класс для обработки запросов на получение списка блюд доступных для заказа.
    """
    def get(self, request):
        dishes = Dish.objects.filter(
            quantity__gt=0
        )
        serializer = DishSerializer(
            dishes,
            many=True,
            remove_fields=['created_at', 'updated_at']
        )
        return Response(serializer.data)


class GetOrderDataByOrderId(APIView):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)