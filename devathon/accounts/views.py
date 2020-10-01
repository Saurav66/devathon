from django.shortcuts import render

from django.contrib.auth import authenticate, login

def my_view(request):
    regid = request.POST['regid']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def order(request):
    return render(request, 'accounts/order.html')