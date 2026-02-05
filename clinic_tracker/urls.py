from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

from clinic.views import dashboard, login_view, logout_view, public_view

urlpatterns = [
    path("", lambda request: redirect("/admin/")),
    path("admin/", admin.site.urls),
    path("dashboard/", dashboard, name="dashboard"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("p/<str:token>/", public_view, name="public"),
]

