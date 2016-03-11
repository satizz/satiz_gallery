from django.contrib import admin
from bought.models import item
from night_market_purchase.models import buy_item, bought

# Register your models here.
admin.site.register(buy_item)
admin.site.register(bought)