from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm, PasswordResetForm

User = get_user_model()


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
        model = User
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
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already used")
        return email


class SetPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword',
            'placeholder': 'Password',
        }),
        label='Password'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingPassword2',
            'placeholder': 'Password',
        }),
        label='Confirm your password'
    )



class PasswordResetEmailForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'placeholder': 'Email address ',
        }),
        label='Email address'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError("This email isn't exist")
