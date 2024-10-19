from django.contrib import admin
from .models import *

# Register your models here.

class womenAdmin(admin.ModelAdmin):
    list_display = ['id','dress_name','price','category','created_at']

admin.site.register(WomenDresesItems,womenAdmin)
