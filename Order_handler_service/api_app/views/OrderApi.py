from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..authentications import JWTAuthentication
from ..models import Dish, Order, OrderDish
from ..serializers import DishSerializer, OrderSerializer


class CreateOrder(APIView):
    """
    Конечная точка для создания заказа.
    Accepts only POST requests with JWT token in headers.
    """
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        user_id = request.user.get('user_id')
        special_requests = request.data.get('special_requests', '')

        dishes_data = request.data.get('dishes', [])

        if not dishes_data:
            # Проверка на наличие блюд в запросе заказа
            return Response(
                {"detail": "The list of dishes cannot be empty."},
                status=status.HTTP_400_BAD_REQUEST
            )

        dish_ids = [dish.get('dish_id') for dish in dishes_data]

        dishes = Dish.objects.in_bulk(dish_ids)

        if len(dishes) != len(dish_ids):
            # Проверка на наличие всех блюд в базе данных по их id
            missing_ids = set(dish_ids) - set(dishes.keys())
            return Response(
                {"detail": f"Dishes with IDs {', '.join(map(str, missing_ids))} were not found."},
                status=status.HTTP_400_BAD_REQUEST
            )

        for dish_data in dishes_data:
            # Проверка на наличие достаточного количества блюд

            dish = dishes[dish_data.get('dish_id')]

            if dish_data.get('quantity') is None or dish_data.get('quantity') <= 0:
                return Response(
                    {"detail": f"The quantity for dish with ID {dish.id} is not specified."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if dish.quantity < dish_data.get('quantity'):
                return Response(
                    {"detail": f"Insufficient quantity of dish with ID {dish.id} in stock."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        order = Order.objects.create(
            user_id=user_id,
            special_requests=special_requests
        )

        for dish_in_order in dishes_data:
            # Уменьшаем количество товаров в наличии
            dishes[dish_in_order.get('dish_id')].quantity -= dish_in_order.get('quantity')
            dishes[dish_in_order.get('dish_id')].save()

            OrderDish.objects.create(
                order=order,
                dish_id=dishes[dish_in_order.get('dish_id')],
                quantity=dish_in_order.get('quantity'),
                price=dishes[dish_in_order.get('dish_id')].price
            )

        return Response({'message': 'Order created'})


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
    """
    Класс для обработки запросов на получение данных заказа по его id.
    Возвращает данные заказа и список блюд в нем.
    """

    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
