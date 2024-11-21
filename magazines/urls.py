from django.contrib import admin
from django.urls import path
from . import views


app_name = "magazines"

urlpatterns = [
    path("",views.magazines,name = "magazines"),
    path("addmagazine/",views.addMagazine,name = "addmagazine"),
    path("dashmag/", views.dashmag, name = "dashmag"),
    path("magazine/<int:id>", views.detail,name = "detail"),
    path("update/<int:id>",views.updateMagazine,name = "update",),
]
