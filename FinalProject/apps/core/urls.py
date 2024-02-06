from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from . import views


urlpatterns = [
    path("", index, name="index"),
    path("Login/", CustomLoginView.as_view(), name="login"),
    path("Register/", register, name="register"),
    path("Vegetable/list", views.vegetable_list, name="vegetable_list"),
]
