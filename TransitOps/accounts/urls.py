from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="login", permanent=False)),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),
    path(
        "delete-account/",
        views.delete_account,
        name="delete_account"
    ),
    path(
        "delete-profile-image/",
        views.delete_profile_image,
        name="delete_profile_image"
    ),
]