from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import (
    SignInTokenObtainPairSerializer,
    SignUpSerializer
)


class SignInTokenObtainPairView(TokenObtainPairView):
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
