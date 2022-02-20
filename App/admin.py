from django.contrib import admin
from .models import Vehicles
# Register your models here.

@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('Vehicle_Name','Speed','Average_Speed','Temperature','Fuel_level','Engine_Status')
