from django.contrib import admin

from .models import Appartment  , Object , Block

@admin.register(Appartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'area', 'floor', 'rooms_count', 'deadline', 'type')
    list_filter = ('type', 'floor')
    search_fields = ('number', )
    
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'addres')
    search_fields = ('name', 'addres')
    list_filter = ('name', 'addres')
    
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('number', 'floors_count', 'entrance_count', 'image')
    search_fields = ('number', )
    list_filter = ('number', 'floors_count', 'entrance_count')
    

    
