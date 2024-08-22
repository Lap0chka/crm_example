from . import views
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # Sign in/up and Logout
    path('sign-in/', views.login_user, name='login'),
    path('sign-up/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),



    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]
