from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Trip, TripAssignment, TripStatusHistory
from .forms import (
    TripForm,
    TripAssignmentForm,
    TripStatusHistoryForm,
)

from fleet.models import Vehicle, Driver

@login_required
def trip_list(request):

    trips = Trip.objects.all().order_by("-created_at")

    context = {
        "trips": trips
    }

    return render(
        request,
        "trips/trip_list.html",
        context
    )

@login_required
def trip_create(request):

    if request.method == "POST":

        form = TripForm(request.POST)

        if form.is_valid():

            trip = form.save(commit=False)

            # Trip status is Pending by default
            trip.status = "Pending"

            trip.save()

            messages.success(
                request,
                "Trip created successfully."
            )

            return redirect("trips:trip_list")

    else:

        form = TripForm()

    context = {
        "form": form
    }

    return render(
        request,
        "trips/trip_form.html",
        context
    )
@login_required
def trip_detail(request, pk):

    trip = get_object_or_404(
        Trip,
        pk=pk
    )

    assignment = TripAssignment.objects.filter(
        trip=trip
    ).first()

    status_history = TripStatusHistory.objects.filter(
        trip=trip
    ).order_by("-changed_at")

    context = {
        "trip": trip,
        "assignment": assignment,
        "status_history": status_history,
    }

    return render(
        request,
        "trips/trip_detail.html",
        context
    )


@login_required
def trip_update(request, pk):

    trip = get_object_or_404(
        Trip,
        pk=pk
    )

    if request.method == "POST":

        form = TripForm(
            request.POST,
            instance=trip
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Trip updated successfully."
            )

            return redirect(
                "trips:trip_detail",
                pk=trip.pk
            )

    else:

        form = TripForm(
            instance=trip
        )

    context = {
        "form": form,
        "trip": trip,
    }

    return render(
        request,
        "trips/trip_form.html",
        context
    )


@login_required
def trip_delete(request, pk):

    trip = get_object_or_404(
        Trip,
        pk=pk
    )

    if request.method == "POST":

        trip.delete()

        messages.success(
            request,
            "Trip deleted successfully."
        )

        return redirect(
            "trips:trip_list"
        )

    context = {
        "trip": trip
    }

    return render(
        request,
        "trips/trip_confirm_delete.html",
        context
    )
@login_required
def trip_assign(request, trip_id):

    trip = get_object_or_404(
        Trip,
        pk=trip_id
    )

    assignment = TripAssignment.objects.filter(
        trip=trip
    ).first()

    if assignment:

        messages.warning(
            request,
            "This trip has already been assigned."
        )

        return redirect(
            "trips:trip_detail",
            pk=trip.pk
        )

    if request.method == "POST":

        form = TripAssignmentForm(request.POST)

        if form.is_valid():

            assignment = form.save(commit=False)

            assignment.trip = trip

            assignment.assigned_by = request.user

            assignment.save()

            vehicle = assignment.vehicle

            driver = assignment.driver

            vehicle.status = "Unavailable"
            vehicle.save()

            driver.status = "Unavailable"
            driver.save()

            old_status = trip.status

            trip.status = "Dispatched"

            trip.save()

            TripStatusHistory.objects.create(
                trip=trip,
                old_status=old_status,
                new_status="Dispatched",
                changed_by=request.user,
                remarks="Trip assigned successfully."
            )

            messages.success(
                request,
                "Trip assigned successfully."
            )

            return redirect(
                "trips:trip_detail",
                pk=trip.pk
            )

    else:

        form = TripAssignmentForm(
            initial={
                "trip": trip
            }
        )

    context = {
        "trip": trip,
        "form": form,
    }

    return render(
        request,
        "trips/trip_assign.html",
        context
    )

@login_required
def trip_change_status(request, trip_id):

    trip = get_object_or_404(
        Trip,
        pk=trip_id
    )

    if request.method == "POST":

        form = TripStatusHistoryForm(request.POST)

        if form.is_valid():

            history = form.save(commit=False)

            history.trip = trip

            history.old_status = trip.status

            history.changed_by = request.user

            history.save()

            trip.status = history.new_status

            trip.save()

            assignment = TripAssignment.objects.filter(
                trip=trip
            ).first()

            if assignment and history.new_status in [
                "Completed",
                "Cancelled",
            ]:

                assignment.vehicle.status = "Available"
                assignment.vehicle.save()

                assignment.driver.status = "Available"
                assignment.driver.save()

            messages.success(
                request,
                "Trip status updated successfully."
            )

            return redirect(
                "trips:trip_detail",
                pk=trip.pk
            )

    else:

        form = TripStatusHistoryForm(
            initial={
                "trip": trip,
                "old_status": trip.status,
            }
        )

    context = {
        "trip": trip,
        "form": form,
    }

    return render(
        request,
        "trips/trip_change_status.html",
        context
    )

@login_required
def trip_status_history(request, trip_id):

    trip = get_object_or_404(
        Trip,
        pk=trip_id
    )

    history = TripStatusHistory.objects.filter(
        trip=trip
    ).order_by("-changed_at")

    context = {
        "trip": trip,
        "history": history,
    }

    return render(
        request,
        "trips/trip_status_history.html",
        context
    )
