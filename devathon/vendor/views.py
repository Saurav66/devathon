from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import authenticate, login


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'vendor/dashboard.html')
    return redirect("/accounts/vendor/")

def order(request):
    if request.user.is_authenticated:
        return render(request, 'vendor/order.html')
    return redirect("/accounts/vendor/")