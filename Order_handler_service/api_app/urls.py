from django.urls import path


from .views import (
    DishGetListAndCreateApi,
    DishUpdateDestroy,
    ListAvailableToOrderDishes
)

urlpatterns = [
    path('dish/', DishGetListAndCreateApi.as_view()),
    path('dish/<int:pk>/', DishUpdateDestroy.as_view()),
    path('get-menu/', ListAvailableToOrderDishes.as_view()),
]
