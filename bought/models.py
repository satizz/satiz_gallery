from __future__ import unicode_literals

from django.db import models

# models are here.

class item(models.Model):
    name = models.CharField(max_length = 60)
    quan = models.IntegerField('Quantity',default = 1)
    rate = models.IntegerField(default = 0)
    date = models.DateField('Bought In')

    def __str__(self):
        return self.name
