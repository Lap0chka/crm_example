from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from account.forms import LoginForm


def dashboard(request):
    return render(request, 'account/dashboard/dashboard.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
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
                messages.error(request, 'Invalid username or password.')
                return redirect('account:login')
    else:
        form = LoginForm()
    return render(request, 'account/login/login.html', {'form': form})
