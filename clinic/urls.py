from django.contrib import admin
from django.urls import path
from clinic.views import dashboard, public_view, login_view, logout_view
from django.shortcuts import redirect

urlpatterns = [
    
    path("", lambda request: redirect("dashboard")),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("p/<str:token>/", public_view, name="public"),
]

