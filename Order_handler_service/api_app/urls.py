from django.urls import path


from .views import DishCrudApi

urlpatterns = [
    path('dish/', DishCrudApi.as_view()),
]
