from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)


class Address(models.Model):
    street = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=50)


class UserDetails(models.Model):
    age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(
        Address, on_delete=SET_NULL, null=True, related_name='user_address')
    country = models.ManyToManyField(Country)


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()

    class Meta:
        abstract = True


class Information(BaseModel):
    info = models.CharField(max_length=100)
    bio = models.TextField()
