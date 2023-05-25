from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import (
    SignInTokenObtainPairSerializer,
    SignUpSerializer
)


class SignInTokenObtainPairView(TokenObtainPairView):
    """
    Api для авторизации пользователя по почте и паролю.
    Переопределяет стандартный сериализатор и вся логика в нем.
    """
    serializer_class = SignInTokenObtainPairSerializer


class SignUpView(APIView):
    def post(self, request, format=None):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(
                    {"message": "success"},
                    status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserDataView(APIView):
    def get(self, request, **kwargs):
        access_token = request.headers.get('Authorization')
        if access_token is None:
            return Response(
                {"message": "token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        access_token = access_token.split(' ')[1]

        jwt_authentication = JWTAuthentication()
        validated_token = jwt_authentication.get_validated_token(access_token)
        user = jwt_authentication.get_user(validated_token)

        return Response({
            "username": user.username,
            "email": user.email,
            "is manager": user.is_staff
        },
            status=status.HTTP_200_OK
        )
