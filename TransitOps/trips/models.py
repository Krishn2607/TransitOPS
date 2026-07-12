from django.db import models
from django.contrib.auth.models import User
from fleet.models import Vehicle, Driver


class Trip(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Dispatched', 'Dispatched'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    trip_id = models.CharField(max_length=20, unique=True)

    source = models.CharField(max_length=100)

    destination = models.CharField(max_length=100)

    cargo_type = models.CharField(max_length=100)

    cargo_weight = models.DecimalField(max_digits=10, decimal_places=2)

    distance = models.DecimalField(max_digits=10, decimal_places=2)

    estimated_duration = models.DurationField()

    revenue = models.DecimalField(max_digits=12, decimal_places=2)

    start_datetime = models.DateTimeField()

    end_datetime = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

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

    assigned_at = models.DateTimeField(auto_now_add=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.trip.trip_id}"
    
class TripStatusHistory(models.Model):

    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        related_name="status_history"
    )

    old_status = models.CharField(max_length=20)

    new_status = models.CharField(max_length=20)

    changed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    changed_at = models.DateTimeField(auto_now_add=True)

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.trip.trip_id} : {self.new_status}"