from django.shortcuts import render, HttpResponseRedirect
from .forms import Vehicle_Form
from .models import Vehicles
from django.http import HttpResponseRedirect

#function for showing List of vehicles:
def Vehicle_List(request):
    vcl_list = Vehicles.objects.all()
    return render(request,"App/Vehicle_List.html",{'vcl_list':vcl_list})
    

#Function for  Vehicle Registration Form & Showing those details into Vehicle_details.html
def Showformdata(request):
    if request.method == 'POST':
        fm = Vehicle_Form(request.POST)
        if fm.is_valid():
            vn = fm.cleaned_data['Vehicle_Name']
            sp = fm.cleaned_data['Speed']
            asp = fm.cleaned_data['Average_Speed']
            temp = fm.cleaned_data['Temperature']
            fl = fm.cleaned_data['Fuel_level']
            es = fm.cleaned_data['Engine_Status']
        reg = Vehicles(Vehicle_Name=vn,Speed=sp, Average_Speed=asp, Temperature=temp, Fuel_level=fl , Engine_Status=es)
        reg.save()
        return render(request, 'App/Vehicle_Details.html', {'Vehicle_Name':vn,'Speed':sp, 'Average_Speed':asp, 'Temperature':temp, 'Fuel_level':fl , 'Engine_Status':es})
    else:
        fm = Vehicle_Form()
    return render(request, 'App/form.html', {'form':fm})


#function fot Editing/ Updating Vehicle Data:
def update_data(request , id):
    if request.method =='POST':
        vecl = Vehicles.objects.get(pk=id)
        fm = Vehicle_Form(request.POST, instance=vecl)
        if fm.is_valid():
            fm.save()
    else:
        vecl = Vehicles.objects.get(pk=id)
        fm = Vehicle_Form(instance=vecl)

    return render(request, 'App/update_vehicle.html', {'form':fm})


#function for Deleting any Vehicle form the List and Backend:
def vehicle_delete(request,id):
    if request.method =='POST':
        vecl = Vehicles.objects.get(pk=id)
        vecl.delete()
        return HttpResponseRedirect('/list')

