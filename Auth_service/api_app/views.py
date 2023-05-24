from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import SignInTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = SignInTokenObtainPairSerializer
