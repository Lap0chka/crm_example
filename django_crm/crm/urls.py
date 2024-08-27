from . import views
from django.urls import path

app_name = 'crm'

urlpatterns = [
    path('db-download/', views.db_download, name='db_download'),
]
