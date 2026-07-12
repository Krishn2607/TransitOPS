from django.urls import path

from .views import (
    VehicleListView,
    vehicle_add,
    VehicleDetailView,
    VehicleUpdateView,
    VehicleDeleteView
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

]