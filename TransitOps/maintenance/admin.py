from django.contrib import admin
from .models import Maintenance


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle",
        "issue_title",
        "status",
        "priority",
        "scheduled_date",
        "estimated_cost",
    )

    search_fields = (
        "vehicle__registration_number",
        "issue_title",
    )

    list_filter = (
        "status",
        "priority",
    )