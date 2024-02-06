from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import *
from . import models

def index(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:index")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})

def vegetable_list(request):
    consult = models.Vegetable.objects.all()
    context = {"vegetables": consult}
    return render(request, "core/vegetable_list.html", context)