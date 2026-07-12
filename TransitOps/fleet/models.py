from django.db import models

class Vehicle(models.Model):

    VEHICLE_TYPE_CHOICES = [
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Mini Truck', 'Mini Truck'),
        ('Trailer', 'Trailer'),
        ('Container', 'Container'),
        ('Other', 'Other'),
    ]

    VEHICLE_STATUS_CHOICES = [
        ('Available', 'Available'),
        ('On Trip', 'On Trip'),
        ('In Maintenance', 'In Maintenance'),
        ('Retired', 'Retired'),
    ]

    INDIAN_STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
        ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
        ('Chandigarh', 'Chandigarh'),
        ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('Delhi', 'Delhi'),
        ('Jammu and Kashmir', 'Jammu and Kashmir'),
        ('Ladakh', 'Ladakh'),
        ('Lakshadweep', 'Lakshadweep'),
        ('Puducherry', 'Puducherry'),
    ]

    registration_number = models.CharField(
        max_length=20,
        unique=True
    )

    manufacturer = models.CharField(
        max_length=100
    )

    vehicle_model = models.CharField(
        max_length=100
    )

    manufacturing_year = models.PositiveIntegerField()

    vehicle_type = models.CharField(
        max_length=20,
        choices=VEHICLE_TYPE_CHOICES
    )

    capacity = models.PositiveIntegerField(
        help_text="Maximum cargo capacity in KG"
    )

    odometer_reading = models.PositiveIntegerField(
        help_text="Current odometer reading in KM"
    )

    acquisition_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    purchase_date = models.DateField()

    state = models.CharField(
        max_length=50,
        choices=INDIAN_STATE_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=VEHICLE_STATUS_CHOICES,
        default='Available'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.registration_number} - {self.manufacturer} {self.vehicle_model}"

    class Meta:
        ordering = ['registration_number']
