from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .CustomUserManager import UserManager


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
    updated_at = models.DateTimeField(auto_now=True)  # оно само будет обновляться при изменении записи

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # Поле, которое будет использоваться для входа в систему
    REQUIRED_FIELDS = ['username']  # Обязательные поля для создания пользователя

    objects = UserManager()  # указываем менеджер для данной модели

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        return self