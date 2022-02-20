from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Showformdata),
    path('add_new_vehicle/',views.Showformdata,name="add_new"),
    path('list/',views.Vehicle_List, name="vehicle_list"),
    path('delete/<int:id>/',views.vehicle_delete,name='vehicle_delete'),
    path('<int:id>/',views.update_data ,name='update_data'),
]