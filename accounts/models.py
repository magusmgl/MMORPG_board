from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class OneTimeCode(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE)

    code = models.SmallIntegerField()
