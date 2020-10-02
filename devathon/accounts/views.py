from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login/student/") 
    return render(request, 'accounts/student/index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/student/index.html')
    return redirect("/accounts/student/")

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/accounts/home/")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("/accounts/student/")
            
    return HttpResponse('404 - Not Found')

def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("/accounts/student/")
