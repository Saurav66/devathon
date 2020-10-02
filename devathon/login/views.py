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
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/accounts/dashboard")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login/student/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login/student/")

def handleLogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/accounts/dashboard")
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect("/login/student/")
            
    return HttpResponse('404 - Not Found')

def handleLogout(request): 
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home') 
