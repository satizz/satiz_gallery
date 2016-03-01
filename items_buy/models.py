from __future__ import unicode_literals
from datetime import date
from django.db import models

# models are here.

class items(models.Model):
    name = models.CharField(max_length = 60)
    rate = models.IntegerField(default = 0)
    quan = models.IntegerField(default = 1)
    buyed = date()

    def __str__(self):
        return self.name


