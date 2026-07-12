from django.urls import path
from .views import VehicleListView, vehicle_add


urlpatterns = [
    path(
        "vehicles/",
        VehicleListView.as_view(),
        name="vehicle_list"
    ),

    path(
        "vehicles/add/",
        vehicle_add,
        name="vehicle_add"
    ),
]