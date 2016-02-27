from django.db import models

# Models here.

class item_detail(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    quantity = models.IntegerField(default = 1)
    Buy_date = models.DateField('date purchased')
    
    def __str__(self):
        return self.name()
    
class status(models.Model):
    YN = (('Y','Sold'),('N','Not Sold'))
    item = models.ForeignKey(item_detail)
    quantity = models.IntegerField(default = 1)
    sold = models.CharField(max_length = 1,choices = YN)
    
    def __str__(self):
        return item+'is'+sold
    
    