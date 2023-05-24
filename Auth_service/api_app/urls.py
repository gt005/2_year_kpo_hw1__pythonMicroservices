from django.urls import path

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('sign-in/', MyTokenObtainPairView.as_view(), name='sing-in'),
    path('sign-in/refresh_token/', TokenRefreshView.as_view(),
         name='token_refresh'),

]