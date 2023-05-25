from rest_framework import authentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None

        token = auth_header.split(' ')[1]
        try:
            jwt_token = AccessToken(token)
        except Exception as e:
            raise exceptions.AuthenticationFailed('Invalid token')

        return (jwt_token, None)  # (user, auth) в стандарте BaseAuthentication
