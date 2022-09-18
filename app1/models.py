from re import T
from django.db import models

class TestModel(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True)
    car = models.CharField(max_length=100, null=True)
    song = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=13, null=True)

    def __str__(self) -> str:
        return self.first_name


