from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from fleet.models import Vehicle, Driver
from trips.models import Trip
from maintenance.models import Maintenance


@login_required
def dashboard(request):

    # ===============================
    # Dashboard Cards
    # ===============================

    total_vehicles = Vehicle.objects.count()
    total_drivers = Driver.objects.count()
    total_trips = Trip.objects.count()

    available_vehicles = Vehicle.objects.filter(
        status="Available"
    ).count()

    vehicles_on_trip = Vehicle.objects.filter(
        status="On Trip"
    ).count()

    vehicles_in_maintenance = Vehicle.objects.filter(
        status="In Maintenance"
    ).count()

    pending_trips = Trip.objects.filter(
        status="Pending"
    ).count()

    dispatched_trips = Trip.objects.filter(
        status="Dispatched"
    ).count()

    in_progress_trips = Trip.objects.filter(
        status="In Progress"
    ).count()

    completed_trips = Trip.objects.filter(
        status="Completed"
    ).count()

    cancelled_trips = Trip.objects.filter(
        status="Cancelled"
    ).count()

    pending_maintenance = Maintenance.objects.filter(
        status="Pending"
    ).count()

    scheduled_maintenance = Maintenance.objects.filter(
        status="Scheduled"
    ).count()

    maintenance_in_progress = Maintenance.objects.filter(
        status="In Progress"
    ).count()

    completed_maintenance = Maintenance.objects.filter(
        status="Completed"
    ).count()

    # ===============================
    # Revenue
    # ===============================

    total_revenue = 0

    for trip in Trip.objects.all():
        total_revenue += trip.revenue

    # ===============================
    # Recent Data
    # ===============================

    recent_trips = Trip.objects.order_by(
        "-created_at"
    )[:5]

    recent_vehicles = Vehicle.objects.order_by(
        "-created_at"
    )[:5]

    recent_maintenance = Maintenance.objects.order_by(
        "-created_at"
    )[:5]

    # ===============================
    # Context
    # ===============================

    context = {

        # Dashboard Cards
        "total_vehicles": total_vehicles,
        "total_drivers": total_drivers,
        "total_trips": total_trips,
        "total_revenue": total_revenue,

        # Vehicle Statistics
        "available_vehicles": available_vehicles,
        "vehicles_on_trip": vehicles_on_trip,
        "vehicles_in_maintenance": vehicles_in_maintenance,

        # Trip Statistics
        "pending_trips": pending_trips,
        "dispatched_trips": dispatched_trips,
        "in_progress_trips": in_progress_trips,
        "completed_trips": completed_trips,
        "cancelled_trips": cancelled_trips,

        # Maintenance Statistics
        "pending_maintenance": pending_maintenance,
        "scheduled_maintenance": scheduled_maintenance,
        "maintenance_in_progress": maintenance_in_progress,
        "completed_maintenance": completed_maintenance,

        # Recent Tables
        "recent_trips": recent_trips,
        "recent_vehicles": recent_vehicles,
        "recent_maintenance": recent_maintenance,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )