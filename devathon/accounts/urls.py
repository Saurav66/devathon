from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('student/',auth_views.LoginView.as_view(template_name='accounts/student/login.html'), name='studentlogin'),
    path('vendor/',auth_views.LoginView.as_view(template_name='accounts/vendor/login.html'), name='vendorlogin'),
    path('studentlogin/', views.handleLogin, name='handleStudentLogin'),
    path('vendorlogin/', views.handleLogin, name='handleStudentLogin'),
    path('logut/', views.handleLogout, name='handleLogout'),
    path('home/', views.home, name='home'),
]