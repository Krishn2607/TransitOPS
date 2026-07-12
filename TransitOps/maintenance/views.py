from django.shortcuts import render, redirect, get_object_or_404
from .models import Maintenance
from .forms import MaintenanceForm


def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    return render(request, "maintenance/maintenance_list.html", {
        "maintenances": maintenances
    })


def maintenance_create(request):
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("maintenance_list")
    else:
        form = MaintenanceForm()

    return render(request, "maintenance/maintenance_form.html", {
        "form": form
    })


def maintenance_update(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)

    if request.method == "POST":
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect("maintenance_list")
    else:
        form = MaintenanceForm(instance=maintenance)

    return render(request, "maintenance/maintenance_form.html", {
        "form": form
    })


def maintenance_delete(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)

    if request.method == "POST":
        maintenance.delete()
        return redirect("maintenance_list")

    return render(request, "maintenance/maintenance_confirm_delete.html", {
        "maintenance": maintenance
    })
    
def maintenance_detail(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)

    return render(
        request,
        "maintenance/maintenance_detail.html",
        {
            "maintenance": maintenance
        }
    )