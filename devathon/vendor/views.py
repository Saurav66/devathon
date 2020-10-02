from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login


def dashboard(request):
    return render(request, 'vendor/dashboard.html')


def order(request):
    return render(request, 'vendor/order.html')
