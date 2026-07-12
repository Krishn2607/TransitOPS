from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Vehicle
from .forms import VehicleForm

class VehicleListView(ListView):
    model = Vehicle
    template_name = "fleet/vehicle_list.html"
    context_object_name = "vehicles"
    paginate_by = 10

def vehicle_add(request):

    if request.method == "POST":

        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("vehicle_list")

    else:

        form = VehicleForm()


    return render(
        request,
        "fleet/vehicle_add.html",
        {
            "form": form
        }
    )