from django.contrib import admin
from bought.models import item

# Register your models here.
class itemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
        ('Quantity',{'fields':['quan']}),
        ('Rate',{'fields':['rate']}),
        ('status',{'fields':['status']}),
    ]
    list_filter = ['date']
    search_fields = ['name']
    list_display = ('name','quan','rate','total')


admin.site.register(item, itemAdmin)