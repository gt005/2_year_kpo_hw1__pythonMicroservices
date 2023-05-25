from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Django требует, чтобы был создан данный менеджер.
    Он помогает работать с бд и создавать пользователей.
    """

    def create_user(self, username: str, email: str, password: str = None):
        """ Создание пользователя по username и email. """
        if username is None:
            raise TypeError('Username не должен быть пустым.')

        if email is None:
            raise TypeError('Почта не должна быть пустой.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Создает и возввращет пользователя с привилегиями суперпользователя.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
