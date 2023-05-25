from django.urls import path


from .views import (
    DishGetListAndCreateApi,
    DishUpdateDestroy,
    ListAvailableToOrderDishes,
    GetOrderDataByOrderId
)

urlpatterns = [
    path('dish/', DishGetListAndCreateApi.as_view()),
    path('dish/<int:pk>/', DishUpdateDestroy.as_view()),
    path('get-menu/', ListAvailableToOrderDishes.as_view()),
    path('get-order-data/<int:id>/', GetOrderDataByOrderId.as_view()),
]
