from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User

from .forms import RegisterForm
from .models import Profile


# ---------------- Register ----------------

def register(request):

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

            messages.success(request, "Account created successfully.")
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

            return redirect("dashboard")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


# ---------------- Logout ----------------

@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


# ---------------- Profile ----------------

@login_required
def profile(request):

    profile = Profile.objects.get(user=request.user)

    context = {
        "profile": profile
    }

    return render(request, "accounts/profile.html", context)
