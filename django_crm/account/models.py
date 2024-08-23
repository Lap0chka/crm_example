from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_pics/%Y/%m/', blank=True)