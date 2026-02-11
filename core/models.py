from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('driver', 'Driver'),
        ('passenger', 'Passenger'),
        ('both', 'Driver & Passenger'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='passenger'
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True
    )

    def __str__(self):
        return self.username

