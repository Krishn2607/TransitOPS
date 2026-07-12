from django import forms
from .models import Vehicle, Driver

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = "__all__"

        widgets = {

            "license_expiry_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "date_of_joining": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),

            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "license_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),

            "years_of_experience": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "emergency_contact": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }