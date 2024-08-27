from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class DbClient(models.Model):
    db_name = models.CharField(max_length=50)
    db = models.FileField(upload_to='db')
    db_owner = models.CharField(max_length=50, blank=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


