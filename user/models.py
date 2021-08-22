from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField
# Create your models here.


# class UserDetail(models.Model):
#     phone_number = models.CharField(max_length=100)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# class User(AbstractUser):
#     middle_name = models.CharField(max_length=100)

#     groups = None
#     user_permissions = None
