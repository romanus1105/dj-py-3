from dataclasses import Field
from django.db import models


class Phone(models.Model):
    # id = models.PositiveSmallIntegerField(primary_key=True) # from 0 to 32767 are safe
    name = models.CharField(max_length=50, unique=True)
    price = models.PositiveIntegerField() # from 0 to 2147483647 are safe
    image = models.URLField() # default max len = 200
    release_date = models.CharField(max_length=10) # because dd.mm.yyyy = 10 symbols
    lte_exists = models.BooleanField() # default is None
    slug = models.CharField(max_length=50, unique=True) # As slug is a derivative of name, 50 is enough
