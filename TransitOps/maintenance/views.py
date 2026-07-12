from datetime import date

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_roles

from .models import Maintenance
from .forms import MaintenanceForm


# ==========================
# Dashboard / List
# ==========================

@login_required
@allowed_roles(["Fleet Manager", "Safety Officer"])
def maintenance_list(request):

    maintenances = Maintenance.objects.all().order_by("-created_at")

    total_jobs = maintenances.count()

    pending_jobs = maintenances.filter(status="Pending").count()

    in_progress_jobs = maintenances.filter(status="In Progress").count()

    completed_jobs = maintenances.filter(status="Completed").count()

    critical_jobs = maintenances.filter(priority="Critical").count()

    today_jobs = maintenances.filter(
        scheduled_date=date.today()
    ).count()

    total_cost = (
        maintenances.aggregate(
            Sum("estimated_cost")
        )["estimated_cost__sum"] or 0
    )

    context = {
        "maintenances": maintenances,
        "total_jobs": total_jobs,
        "pending_jobs": pending_jobs,
        "in_progress_jobs": in_progress_jobs,
        "completed_jobs": completed_jobs,
        "critical_jobs": critical_jobs,
        "today_jobs": today_jobs,
        "total_cost": total_cost,
    }

    return render(
        request,
        "maintenance/maintenance_list.html",
        context,
    )


# ==========================
# Detail
# ==========================

@login_required
@allowed_roles(["Fleet Manager", "Safety Officer"])
def maintenance_detail(request, pk):

    maintenance = get_object_or_404(
        Maintenance,
        pk=pk
    )

    return render(
        request,
        "maintenance/maintenance_detail.html",
        {
            "maintenance": maintenance
        }
    )


# ==========================
# Create
# ==========================

@login_required
@allowed_roles(["Fleet Manager", "Safety Officer"])
def maintenance_create(request):

    if request.method == "POST":

        form = MaintenanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("maintenance_list")

    else:

        form = MaintenanceForm()

    return render(
        request,
        "maintenance/maintenance_form.html",
        {
            "form": form
        }
    )


# ==========================
# Update
# ==========================

@login_required
@allowed_roles(["Fleet Manager", "Safety Officer"])
def maintenance_update(request, pk):

    maintenance = get_object_or_404(
        Maintenance,
        pk=pk
    )

    if request.method == "POST":

        form = MaintenanceForm(
            request.POST,
            instance=maintenance
        )

        if form.is_valid():

            form.save()

            return redirect("maintenance_list")

    else:

        form = MaintenanceForm(
            instance=maintenance
        )

    return render(
        request,
        "maintenance/maintenance_form.html",
        {
            "form": form
        }
    )


# ==========================
# Delete
# ==========================

@login_required
@allowed_roles(["Fleet Manager"])
def maintenance_delete(request, pk):

    maintenance = get_object_or_404(
        Maintenance,
        pk=pk
    )

    if request.method == "POST":

        maintenance.delete()

        return redirect("maintenance_list")

    return render(
        request,
        "maintenance/maintenance_confirm_delete.html",
        {
            "maintenance": maintenance
        }
    )