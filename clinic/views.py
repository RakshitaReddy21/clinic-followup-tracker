from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import FollowUp


@login_required
def dashboard(request):
    followups = FollowUp.objects.all()
    return render(request, "clinic/dashboard.html", {"followups": followups})


def public_view(request,token):
    followups = FollowUp.objects.all()
    return render(request, "clinic/public.html", {"followups": followups})


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return redirect("dashboard")

    return render(request, "clinic/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

