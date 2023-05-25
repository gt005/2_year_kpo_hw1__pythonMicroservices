from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..permissions import IsManager
from ..authentications import JWTAuthentication


class DishCrudApi(APIView):
    """
    Класс для обработки запросов на создание, удаление, изменение и получение
    блюд.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        """
        Получение списка блюд.
        """
        print(request.headers.get('Authorization'))
        return Response({'message': 'Hello, world!'})
