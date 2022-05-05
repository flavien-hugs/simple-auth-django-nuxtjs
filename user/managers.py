# accounts.managers.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):

        if not phone:
            raise ValueError(
                "Le téléphone donné doit être défini"
            )

        now = timezone.now()
        self.phone = phone
        user = self.model(
            phone=phone,
            is_active=True,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                "Le super-utilisateur doit avoir is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                "Le super-utilisateur doit avoir is_superuser=True.")

        return self._create_user(phone, password, **extra_fields)
