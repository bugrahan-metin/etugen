from django.contrib import admin
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("",views.posts,name = "posts"),
    path("addpost/",views.addPost,name = "addpost"),
    path("dashpost/",views.dashpost, name = "dashpost"),
    path("posts/<int:id>",views.detail,name = "detail"),
    path("delete/<int:id>",views.deletePost, name = "delete"),
]