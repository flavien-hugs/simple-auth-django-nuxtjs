# user.models.py

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import(
    AbstractUser, PermissionsMixin
)
from django.core.validators import RegexValidator

from user.managers import UserManager


NULL_AND_BLANK = {'null': True, 'blank': True}
phone_regex = RegexValidator(
    regex='^\+?1?\d{9,15}$',
    message="""
        Le numéro de téléphone doit être saisi dans le format:
        '+999999999'. Un maximum de 15 chiffres est autorisé.
    """
)


class User(AbstractUser, PermissionsMixin):

    username = None
    phone = models.CharField(
        max_length=15,
        unique=True,
        validators=[phone_regex],
        verbose_name='Téléphone',
    )

    objects = UserManager()

    EMAIL_FIELD = 'phone'
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['password']

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = 'comptes'
        indexes = [models.Index(fields=['id'])]

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    def __str__(self) -> str:
        return self.phone
