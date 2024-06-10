from django.contrib import admin
from .models import *

admin.site.register(Kitchen)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['dish_name', 'kitchen_type', 'quantity']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'home_adress']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['owner', 'delivery_date']

# Register your models here.
