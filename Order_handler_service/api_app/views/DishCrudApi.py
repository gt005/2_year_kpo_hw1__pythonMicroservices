from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import mixins

from ..permissions import IsManager
from ..authentications import JWTAuthentication
from ..models import Dish
from ..serializers import DishSerializer


class DishGetListAndCreateApi(ListCreateAPIView):
    """
    Класс для обработки запросов на получение списка блюд и создание новых.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishUpdateDestroy(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)