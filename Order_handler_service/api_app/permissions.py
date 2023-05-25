from rest_framework import permissions
from rest_framework_simplejwt.tokens import AccessToken


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        access_token = request.headers.get('Authorization')
        if access_token is None:
            return False

        access_token = access_token.split(' ')[1]
        token = AccessToken(access_token)

        is_staff = token.get('is_staff', False)

        return is_staff