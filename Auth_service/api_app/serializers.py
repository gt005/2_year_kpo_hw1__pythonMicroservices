from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class SignInTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Переопределяем стандартный сериализатор для получения токена со
    статусом(ролью) пользователя и его id.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавляем поля для is_staff и user_id в токен
        token['is_staff'] = user.is_staff
        token['user_id'] = user.id

        return token


class SignUpSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    Автоматически все поля валидируются и сохраняются в БД.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user