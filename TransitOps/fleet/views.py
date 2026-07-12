from django.shortcuts import render
from django.views.generic import ListView
from .models import Vehicle

class VehicleListView(ListView):
    model = Vehicle
    template_name = "fleet/vehicle_list.html"
    context_object_name = "vehicles"
    paginate_by = 10
