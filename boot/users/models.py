from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_("Username"), unique=True, max_length=120)
    email = models.EmailField(_("Email"), unique=True)
    banned = models.BooleanField(default=False)
    blackListEmail = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
