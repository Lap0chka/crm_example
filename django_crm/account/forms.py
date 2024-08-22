from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'Email address or username',
        }),
        label='Email address or username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
            'placeholder': 'Password',
        }),
        label='Password'
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingText',
            'placeholder': 'Username',
        }),
        label='Username'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'Email address ',
        }),
        label='Email address'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
            'placeholder': 'Password',
        }),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword2',
            'placeholder': 'Password',
        }),
        label='Confirm your password'
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')