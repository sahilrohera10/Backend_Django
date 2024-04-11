from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)