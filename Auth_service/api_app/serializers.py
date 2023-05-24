from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignInTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавляем поля для is_staff и user_id в токен
        token['is_staff'] = user.is_staff
        token['user_id'] = user.id

        return token
