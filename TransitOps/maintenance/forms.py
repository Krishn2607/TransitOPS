from django import forms
from .models import Maintenance


class MaintenanceForm(forms.ModelForm):

    class Meta:
        model = Maintenance
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })