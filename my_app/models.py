from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.


class Address(models.Model):
    name = models.CharField(max_length=50)


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, null=True, related_name='address_person')


class PersonDetail(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)


class Publication(models.Model):
    title = models.CharField(max_length=50)


class Article(models.Model):
    headline = models.CharField(max_length=50)
    publication = ManyToManyField(Publication)
