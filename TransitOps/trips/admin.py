from django.contrib import admin
from .models import Trip, TripAssignment, TripStatusHistory

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = (
        "trip_id",
        "source",
        "destination",
        "status",
        "start_datetime",
    )

    search_fields = (
        "trip_id",
        "source",
        "destination",
    )

    list_filter = (
        "status",
    )

    ordering = (
        "-created_at",
    )


@admin.register(TripAssignment)
class TripAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "trip",
        "vehicle",
        "driver",
        "assigned_by",
        "assigned_at",
    )

    search_fields = (
        "trip__trip_id",
        "vehicle__registration_number",
        "driver__driver_name",
    )

    ordering = (
        "-assigned_at",
    )


@admin.register(TripStatusHistory)
class TripStatusHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "trip",
        "old_status",
        "new_status",
        "changed_by",
        "changed_at",
    )

    list_filter = (
        "new_status",
    )

    ordering = (
        "-changed_at",
    )