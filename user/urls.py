from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("logout/", views.logoutUser,name = "logout"),
    # path("login/", views.loginUser,name = "login"),
    # path("register/", views.register,name = "register"),
    path("ffa8975/", views.ffa,name = "ffa"),



]