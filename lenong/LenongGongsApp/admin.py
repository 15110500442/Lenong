from django.contrib import admin
from .models import TypeInfo,GoodsInfo

# Register your models here.
class GoodAdmin(admin.ModelAdmin):
    list_display = ('gtitle','gpic','isDelete','gprice','gclick','gunit','gjianjie','gcontent','gpub_date')
class TypeAdmin(admin.ModelAdmin):
    list_display = ('ttitle','isDelete')
admin.site.register(GoodsInfo,GoodAdmin)
