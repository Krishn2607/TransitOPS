from django.urls import path
from . import views

app_name = "trips"

urlpatterns = [

    path(
        "",
        views.trip_list,
        name="trip_list"
    ),

    path(
        "create/",
        views.trip_create,
        name="trip_create"
    ),

    path(
        "<int:pk>/",
        views.trip_detail,
        name="trip_detail"
    ),

    path(
        "<int:pk>/update/",
        views.trip_update,
        name="trip_update"
    ),

    path(
        "<int:pk>/delete/",
        views.trip_delete,
        name="trip_delete"
    ),

    path(
        "<int:trip_id>/assign/",
        views.trip_assign,
        name="trip_assign"
    ),

    path(
        "<int:trip_id>/status/",
        views.trip_change_status,
        name="trip_change_status"
    ),

    path(
        "<int:trip_id>/history/",
        views.trip_status_history,
        name="trip_status_history"
    ),
]