from __future__ import unicode_literals

from django.db import models

# Models here.

class item_detail(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 1)
    date = models.DateField('date purchased')
    
    def __unicode__(self):
        return '%s'  %self.name
    
class status(models.Model):
    YN=(
    ('Y','sold'),
    ('N','not sold')
    )
    item = models.ForeignKey(item_detail)
    date_sold = models.DateField(primary_key = True)
    sold = models.CharField(max_length = 1,choices = YN)
    
    