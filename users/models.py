from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.username
