from django.shortcuts import render
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include, reverse_lazy
from . import views

app_name = 'account'

urlpatterns = [
    # Sign in/up and Logout
    path('sign-in/', views.login_user, name='login'),
    path('sign-up/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # Django_email_verification

    path('email-verification-sent/',
         lambda request: render(request, 'account/email/email-verification-sent.html'),
         name='email_verification_sent'
         ),

    # Password reset
    path('password-reset/', views.PasswordResetEmailView.as_view(
        template_name='account/password/password-reset.html',
        email_template_name='account/password/password_reset_email.html',
        success_url=reverse_lazy('account:password_reset_done')),
         name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password/password-reset-done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', views.PasswordResetConfirmationView.as_view(
        template_name='account/password/password-reset-confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password/password-reset-complete.html'),
         name='password_reset_complete'),
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]
