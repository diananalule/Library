from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=500)
    sex = models.CharField(max_length=10, null=True)
    role = models.CharField(max_length=20, default='Student')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'sex', 'role', 'username']

    def __str__(self):
        return self.email


# Create your models here.
