from rest_framework import serializers

from ..models import Dish


class DishSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(DishSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # сделано чтобы можно было динаимчески удалять поля
            for field_name in remove_fields:
                self.fields.pop(field_name)

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
    class Meta:
        model = Dish
        fields = '__all__'