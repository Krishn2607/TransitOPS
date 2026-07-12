from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterForm, ProfileUpdateForm
from .models import Profile


# ---------------- Register ----------------

def register(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            Profile.objects.create(
                user=user,
                role=form.cleaned_data["role"]
            )

            messages.success(request, "Registration Successful.")
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


# ---------------- Login ----------------

def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome Back!")
            return redirect("dashboard")

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "accounts/login.html")


# ---------------- Logout ----------------

@login_required
def logout_view(request):

    logout(request)
    messages.success(request, "Logged Out Successfully")

    return redirect("login")


# ---------------- Profile ----------------

@login_required
def profile(request):

    profile = request.user.profile

    context = {
        "profile": profile
    }

    return render(request, "accounts/profile.html", context)


# ---------------- Edit Profile ----------------

@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == "POST":

        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile,
            user=request.user
        )

        if form.is_valid():

            request.user.first_name = form.cleaned_data["first_name"]
            request.user.last_name = form.cleaned_data["last_name"]
            request.user.email = form.cleaned_data["email"]

            request.user.save()

            form.save()

            messages.success(request, "Profile Updated Successfully")

            return redirect("profile")

    else:

        form = ProfileUpdateForm(
            instance=profile,
            user=request.user
        )

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form}
    )


# ---------------- Change Password ----------------

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            messages.success(request, "Password Changed Successfully")

            return redirect("profile")

    else:

        form = PasswordChangeForm(request.user)

    return render(
        request,
        "accounts/change_password.html",
        {"form": form}
    )

@login_required
def delete_account(request):

    if request.method == "POST":

        request.user.delete()

        return redirect("login")

    return render(
        request,
        "accounts/delete_account.html"
    )

import os

@login_required
def delete_profile_image(request):

    profile = request.user.profile

    if profile.profile_image:

        profile.profile_image.delete(save=False)

        profile.profile_image = None

        profile.save()

    return redirect("profile")