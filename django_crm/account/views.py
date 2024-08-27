from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm

from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
from django.shortcuts import render, redirect
from django_email_verification import send_email
from account.forms import LoginForm, RegisterForm, SetPasswordResetForm, PasswordResetEmailForm


def dashboard(request):
    return render(request, 'account/dashboard/dashboard.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is None:
                user = authenticate(request, email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:dashboard')
            else:
                form.add_error(None, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')

    else:
        form = LoginForm()

    return render(request, 'account/sign/sign_in.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('account:login')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username, email, password)
            send_email(user)
            messages.success(request, 'Account was created successfully.')
            return redirect('/account/email-verification-sent/')
        else:
            messages.error(request, 'Invalid form submission.')
            return redirect('account:register')
    else:
        form = RegisterForm()

    return render(request, 'account/sign/sign_up.html', {'form': form})


class PasswordResetConfirmationView(PasswordResetConfirmView):
    form_class = SetPasswordResetForm

class PasswordResetEmailView(PasswordResetView):
    form_class = PasswordResetEmailForm

    def form_invalid(self, form):
        for error in form.errors.values():
            messages.error(self.request, error)
        return redirect('account:password_reset')


# @login_required
# def db_download(request):
#     if request.method == 'POST':
#         form = DbDownloaderForm(request.POST, request.FILES)
#         if form.is_valid():
#             pass
#     else:
#         form = DbDownloaderForm()
#     return render(request, 'account/dashboard/download/download_db.html', {'form': form})