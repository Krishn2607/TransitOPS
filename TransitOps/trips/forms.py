from django import forms
from .models import Trip, TripAssignment, TripStatusHistory
from fleet.models import Vehicle, Driver


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip

        fields = [
            "source",
            "destination",
            "cargo_type",
            "cargo_weight",
            "distance",
            "estimated_duration",
            "revenue",
            "start_datetime",
            "end_datetime",
            "remarks",
        ]

        widgets = {
            "source": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "destination": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "cargo_type": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "cargo_weight": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "distance": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "estimated_duration": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Duration in Minutes"
                }
            ),

            "revenue": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "start_datetime": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "end_datetime": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),
        }


class TripAssignmentForm(forms.ModelForm):

    class Meta:
        model = TripAssignment

        fields = [
            "trip",
            "vehicle",
            "driver",
            "notes",
        ]

        widgets = {
            "trip": forms.Select(
                attrs={"class": "form-select"}
            ),

            "vehicle": forms.Select(
                attrs={"class": "form-select"}
            ),

            "driver": forms.Select(
                attrs={"class": "form-select"}
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["vehicle"].queryset = Vehicle.objects.filter(
            status="Available"
        )

        self.fields["driver"].queryset = Driver.objects.filter(
            status="Available"
        )


class TripStatusHistoryForm(forms.ModelForm):

    class Meta:
        model = TripStatusHistory

        fields = [
            "new_status",
            "remarks",
        ]

        widgets = {
            "new_status": forms.Select(
                attrs={"class": "form-select"}
            ),

            "remarks": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),
        }