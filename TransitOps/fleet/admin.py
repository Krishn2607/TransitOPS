
from django.contrib import admin
from .models import Vehicle, Driver

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "registration_number",
        "manufacturer",
        "vehicle_model",
        "vehicle_type",
        "capacity",
        "state",
        "status",
    )

    list_filter = (
        "vehicle_type",
        "status",
        "state",
        "manufacturing_year",
    )

    search_fields = (
        "registration_number",
        "manufacturer",
        "vehicle_model",
    )

    ordering = ("registration_number",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 10


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "license_number",
        "phone_number",
        "email",
        "years_of_experience",
        "status",
    )

    list_filter = (
        "status",
        "years_of_experience",
    )

    search_fields = (
        "full_name",
        "license_number",
        "phone_number",
        "email",
    )

    ordering = ("full_name",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 10