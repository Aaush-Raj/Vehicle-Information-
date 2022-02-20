from django import forms
from .models import Vehicles
from django.core import validators

class Vehicle_Form(forms.ModelForm):

    class Meta:
        model = Vehicles
        fields = ('Vehicle_Name','Speed','Average_Speed','Temperature','Fuel_level','Engine_Status')
