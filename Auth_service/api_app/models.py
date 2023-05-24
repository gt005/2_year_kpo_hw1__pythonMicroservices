from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


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


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Создание кастомного пользователя на основе уже существующей абстракции.
    password_hash и role уже приходят с AbstractBaseUser.
    """

    username = models.CharField(
        max_length=255,
        unique=True,
    )
    email = models.EmailField(  # Это varchar, но с доп. валидацией
        max_length=255,
        unique=True,
        db_index=True  # Ускорение работы с бд (поиска)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # Поле, которое будет использоваться для входа в систему
    REQUIRED_FIELDS = ['username']  # Обязательные поля для создания пользователя

    objects = UserManager()  # указываем менеджер для данной модели

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        return self