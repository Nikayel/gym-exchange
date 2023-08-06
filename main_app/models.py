from django.db import models
from django import forms

# Create your models here.
class Comics(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    written_by = models.CharField(max_length=100)
    characters = models.CharField(max_length=100)

