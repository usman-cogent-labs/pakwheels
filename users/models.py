from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    TYPE_CHOICES = [
        ("ADMIN", "Admin"),
        ("USER",  "User")
    ]
    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default="USER")

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
