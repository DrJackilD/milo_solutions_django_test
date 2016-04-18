import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now


def get_random_integer():
    return random.choice([i for i in range(1, 101)])


class CustomUserModel(AbstractUser):
    date_of_birth = models.DateField(default=now)
    random_int = models.IntegerField(default=get_random_integer,
                                     validators=[
                                         MinValueValidator(1),
                                         MaxValueValidator(100)
                                     ])