from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_email_verification import urls as email_urls

from django_crm import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enterpage.urls', namespace='enter')),
    path('crm/', include('crm.urls', namespace='crm')),
    path('account/', include('account.urls', namespace='account')),

    path('email/', include(email_urls), name='email-verification')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


