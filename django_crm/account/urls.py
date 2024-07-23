from . import views
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # Login and Logout
    path('login/', views.login_user, name='login'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]
