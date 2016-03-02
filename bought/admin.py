from django.contrib import admin
from bought.models import item

# Register your models here.
class itemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Item Details',{'fields':[]}  ),
        (None, {'fields':['name']}),
        (None,{'fields':['quan']}),
        (None,{'fields':['rate']}),
        (None,{'fields':['date']}),
        ('status',{'fields':['status']}),
    ]
    list_filter = ['date']
    search_fields = ['name']
    list_display = ('name','quan','rate','total','status')


admin.site.register(item, itemAdmin)