from django.contrib import admin
from .models import Trip, TripAssignment, TripStatusHistory


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = (
        "trip_id",
        "source",
        "destination",
        "cargo_type",
        "status",
        "start_datetime",
        "end_datetime",
    )

    search_fields = (
        "trip_id",
        "source",
        "destination",
        "cargo_type",
    )

    list_filter = (
        "status",
        "cargo_type",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "start_datetime"

    list_per_page = 10


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
        "driver__full_name",
    )

    list_filter = (
        "vehicle",
        "driver",
    )

    ordering = (
        "-assigned_at",
    )

    readonly_fields = (
        "assigned_at",
    )

    date_hierarchy = "assigned_at"

    list_per_page = 10


@admin.register(TripStatusHistory)
class TripStatusHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "trip",
        "old_status",
        "new_status",
        "changed_by",
        "changed_at",
    )

    search_fields = (
        "trip__trip_id",
        "changed_by__username",
    )

    list_filter = (
        "new_status",
        "changed_at",
    )

    ordering = (
        "-changed_at",
    )

    readonly_fields = (
        "changed_at",
    )

    date_hierarchy = "changed_at"

    list_per_page = 15