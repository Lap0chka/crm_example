from . import views
from django.urls import path

app_name = 'enter'

urlpatterns = [
    path('', views.index, name='index'),
]
