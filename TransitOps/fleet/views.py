from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Vehicle, Driver
from .forms import VehicleForm, DriverForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accounts.decorators import allowed_roles

@method_decorator(
    [login_required, allowed_roles(["Fleet Manager"])],
    name="dispatch"
)
class VehicleListView(ListView):
    model = Vehicle
    template_name = "fleet/vehicle_list.html"
    context_object_name = "vehicles"
    paginate_by = 10


@allowed_roles(["Fleet Manager"])
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

@method_decorator(
    [login_required, allowed_roles(["Fleet Manager"])],
    name="dispatch"
)
class VehicleDetailView(DetailView):

    model = Vehicle
    template_name = "fleet/vehicle_detail.html"
    context_object_name = "vehicle"

@method_decorator(
    [login_required, allowed_roles(["Fleet Manager"])],
    name="dispatch"
)
class VehicleUpdateView(UpdateView):

    model = Vehicle
    form_class = VehicleForm
    template_name = "fleet/vehicle_add.html"
    success_url = reverse_lazy("fleet:vehicle_list")

@method_decorator(
    [login_required, allowed_roles(["Fleet Manager"])],
    name="dispatch"
)
class VehicleDeleteView(DeleteView):

    model = Vehicle
    template_name = "fleet/vehicle_delete.html"
    success_url = reverse_lazy("vehicle_list")

class DriverListView(ListView):

    model = Driver
    template_name = "fleet/driver_list.html"
    context_object_name = "drivers"
    paginate_by = 10

def driver_add(request):

    if request.method == "POST":

        form = DriverForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("driver_list")


    else:

        form = DriverForm()


    return render(
        request,
        "fleet/driver_add.html",
        {
            "form": form
        }
    )
class DriverDetailView(DetailView):

    model = Driver
    template_name = "fleet/driver_detail.html"
    context_object_name = "driver"



class DriverUpdateView(UpdateView):

    model = Driver
    form_class = DriverForm
    template_name = "fleet/driver_add.html"
    success_url = reverse_lazy("driver_list")

class DriverDeleteView(DeleteView):

    model = Driver
    template_name = "fleet/driver_delete.html"
    success_url = reverse_lazy("driver_list")
    success_url = reverse_lazy("fleet:vehicle_list")