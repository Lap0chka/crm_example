from django.contrib import admin
from django.urls import path, include
from django_email_verification import urls as email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls', namespace='crm')),
    path('account/', include('account.urls', namespace='account')),

    path('email/', include(email_urls), name='email-verification')
]
