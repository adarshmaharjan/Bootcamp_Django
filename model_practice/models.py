from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    is_active = models.BooleanField(default=False)
    bio = models.CharField(max_length=200, blank=True)

    def save(self, **kwargs) -> None:

        self.full_clean()
        return super().save(**kwargs)
