from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # SEX = {
    #     ('m', 'male'),
    #     ('f', 'female')
    # }

    # sex = models.CharField(choices=SEX, max_length=1)

    phone_number = models.CharField(max_length=11, null=True)
    last_login = models.DateTimeField(auto_now=True)
