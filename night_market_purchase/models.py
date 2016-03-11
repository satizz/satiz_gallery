from __future__ import unicode_literals

from django.db import models

# Create your models here.
class buy_item(models.Model):
    name = models.CharField(max_length=30)
    rate = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class bought(models.Model):
    date = models.DateField()
    item = models.ForeignKey(buy_item)
    quan = models.IntegerField()

