from django.contrib import admin
from .models import RestaurantData

@admin.register(RestaurantData)
class RestAdmin(admin.ModelAdmin):
    ...