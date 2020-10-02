from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
<<<<<<< HEAD
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order/', views.order, name="order"),
=======
    path('login/',
    auth_views.LoginView.as_view(template_name='accounts/login.html'),
    name='login'),
>>>>>>> 5d5cb851e97d24683abef91dd37af188786079a1
]