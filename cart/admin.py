from django.contrib import admin
from .models import	category,product

# Register your models here.

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
        list_display=['name','slug']
        prepopulated_fields	={'slug':('name',)}
    
@admin.register(product)
class productAdmin(admin.ModelAdmin):
        list_display=['name','slug','price','available',	'created',	'updated']
        list_filter	=	['available','created',	'updated']
        list_editable=	['price',	'available']
        prepopulated_fields	=	{'slug':('name',)}