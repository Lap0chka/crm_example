from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from account.forms import LoginForm, RegisterForm


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
            # send_email
            messages.success(request, 'Account was created successfully.')
            return redirect('account:login')
        else:
            messages.error(request, 'Invalid form submission.')
            return redirect('account:register')
    else:
        form = RegisterForm()

    return render(request, 'account/sign/sign_up.html', {'form': form})
