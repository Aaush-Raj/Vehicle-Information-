from django.db import models

class Vehicles(models.Model):
    Vehicle_Name = models.CharField(max_length=50)
    Speed = models.IntegerField(max_length= 3)
    Average_Speed = models.IntegerField(max_length= 3)
    Temperature = models.IntegerField(max_length= 3)
    Fuel_level = models.CharField(max_length= 10)
    Engine_Status = models.CharField(max_length= 20)

