from django.urls import path
app_name = "fleet"
from .views import (
    VehicleListView,
    vehicle_add,
    VehicleDetailView,
    VehicleUpdateView,
    VehicleDeleteView,

    DriverListView,
    driver_add,
    DriverDetailView,
    DriverUpdateView,
    DriverDeleteView,
)


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


    path(
        "vehicles/<int:pk>/",
        VehicleDetailView.as_view(),
        name="vehicle_detail"
    ),


    path(
        "vehicles/<int:pk>/edit/",
        VehicleUpdateView.as_view(),
        name="vehicle_edit"
    ),


    path(
        "vehicles/<int:pk>/delete/",
        VehicleDeleteView.as_view(),
        name="vehicle_delete"
    ),

    path(
        "drivers/",
        DriverListView.as_view(),
        name="driver_list"
    ),

    path(
        "drivers/add/",
        driver_add,
        name="driver_add"
    ),

    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver_detail"
    ),

    path(
        "drivers/<int:pk>/edit/",
        DriverUpdateView.as_view(),
        name="driver_edit"
    ),

    path(
        "drivers/<int:pk>/delete/",
        DriverDeleteView.as_view(),
        name="driver_delete"
    ),

]