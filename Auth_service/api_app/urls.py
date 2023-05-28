from django.urls import path

from .views import (
    SignInTokenObtainPairView,
    SignUpView,
    GetUserDataView,
)

urlpatterns = [
    path('sign-in/', SignInTokenObtainPairView.as_view(), name='sing-in'),
    path('sign-up/', SignUpView.as_view(), name="register"),
    path('get-user-data/', GetUserDataView.as_view(), name="get-user-data"),
]