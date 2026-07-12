from django.db import models
from django.contrib.auth.models import User
from fleet.models import Vehicle, Driver


class Trip(models.Model):

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Dispatched", "Dispatched"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )

    trip_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    source = models.CharField(
        max_length=100
    )

    destination = models.CharField(
        max_length=100
    )

    cargo_type = models.CharField(
        max_length=100
    )

    cargo_weight = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    distance = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estimated_duration = models.PositiveIntegerField(
        help_text="Estimated Duration (in minutes)"
    )

    revenue = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    start_datetime = models.DateTimeField()

    end_datetime = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new and not self.trip_id:
            self.trip_id = f"TRIP{self.pk:05d}"
            super().save(update_fields=["trip_id"])

    def __str__(self):
        return self.trip_id


class TripAssignment(models.Model):

    trip = models.OneToOneField(
        Trip,
        on_delete=models.CASCADE,
        related_name="assignment"
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE
    )

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.trip.trip_id}"


class TripStatusHistory(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="status_history"
    )

    old_status = models.CharField(
        max_length=20,
        choices=Trip.STATUS_CHOICES
    )

    new_status = models.CharField(
        max_length=20,
        choices=Trip.STATUS_CHOICES
    )

    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    changed_at = models.DateTimeField(
        auto_now_add=True
    )

    remarks = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.trip.trip_id} : {self.new_status}"