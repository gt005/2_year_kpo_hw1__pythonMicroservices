from rest_framework import serializers

from ..models import Dish


class DishSerializer(serializers.ModelSerializer):
    """
    Сериализатор для блюд.
    """
    class Meta:
        model = Dish
        fields = '__all__'