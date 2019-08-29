from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    address = models.CharField(max_length=254, blank=True)
    birthday = models.DateField(null=True)
    description = models.TextField(blank=True)
