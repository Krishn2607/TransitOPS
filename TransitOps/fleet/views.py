from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

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

            return redirect("fleet:vehicle_list")


    else:

        form = VehicleForm()


    return render(
        request,
        "fleet/vehicle_add.html",
        {
            "form": form
        }
    )

class VehicleDetailView(DetailView):

    model = Vehicle
    template_name = "fleet/vehicle_detail.html"
    context_object_name = "vehicle"

class VehicleUpdateView(UpdateView):

    model = Vehicle
    form_class = VehicleForm
    template_name = "fleet/vehicle_add.html"
    success_url = reverse_lazy("fleet:vehicle_list")

class VehicleDeleteView(DeleteView):

    model = Vehicle
    template_name = "fleet/vehicle_delete.html"
    success_url = reverse_lazy("fleet:vehicle_list")