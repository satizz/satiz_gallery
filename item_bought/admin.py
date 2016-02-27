from django.contrib import admin
from .models import item_detail, status
# your models here.

admin.site.register(item_detail)
admin.site.register(status)