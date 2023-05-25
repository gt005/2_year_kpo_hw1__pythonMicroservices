from django.urls import path


from .views import DishGetListAndCreateApi, DishUpdateDestroy

urlpatterns = [
    path('dish/', DishGetListAndCreateApi.as_view()),
    path('dish/<int:pk>/', DishUpdateDestroy.as_view(),
         name='dish-retrieve-update-destroy'),
]
