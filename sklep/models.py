from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    nazwa = models.CharField(max_length=128)
    cena = models.FloatField()