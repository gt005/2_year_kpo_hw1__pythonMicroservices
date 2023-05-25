from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Dish
from ..serializers import DishSerializer


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
