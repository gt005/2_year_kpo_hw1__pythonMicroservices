from rest_framework import serializers

from ..models import Dish


class DishSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format='%d %B %Y %H:%M:%S',
        required=False,
        read_only=True,
    )
    updated_at = serializers.DateTimeField(
        format='%d %B %Y %H:%M:%S',
        required=False,
        read_only=True,
    )

    """
    Сериализатор для блюд.
    """
    class Meta:
        model = Dish
        fields = '__all__'