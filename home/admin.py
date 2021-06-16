from django.contrib import admin
from .models import *
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','name','image']

class PreparationAdmin(admin.ModelAdmin):
    list_display = ('id','type','image','recipe','duration','prep','method','utensils','procedure')
admin.site.register(Type,TypeAdmin)
admin.site.register(Preparation,PreparationAdmin) 