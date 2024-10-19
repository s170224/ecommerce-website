from django.contrib import admin

from .models import *

# Register your models here.


class AllFieldsMainAdmin(admin.ModelAdmin):
    list_display = ['id','category']

class AllFieldsAdmin(admin.ModelAdmin):
    list_display = ['id','dress_model_type']

admin.site.register(ShoppingCategory,AllFieldsMainAdmin)
admin.site.register(Womendress,AllFieldsAdmin)
admin.site.register(Kidsdress,AllFieldsAdmin)
admin.site.register(Boysdress,AllFieldsAdmin)

