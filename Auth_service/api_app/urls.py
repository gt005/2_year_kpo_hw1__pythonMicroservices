from django.urls import path

from .views import (
    SignInTokenObtainPairView,
    SignUpView,
    GetUserDataView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('sign-in/', SignInTokenObtainPairView.as_view(), name='sing-in'),
    path('sign-in/refresh_token/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('sign-up/', SignUpView.as_view(), name="register"),
    path('get-user-data/', GetUserDataView.as_view(), name="get-user-data"),
]