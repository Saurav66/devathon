from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('order/', views.order, name="order"),
]