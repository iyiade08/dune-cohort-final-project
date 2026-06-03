from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model  = User
        fields = ['username', 'email', 'phone', 'role', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters.')
        if username and not username.isalnum():
            raise forms.ValidationError('Username can only contain letters and numbers.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.replace('+', '').replace(' ', '').isdigit():
            raise forms.ValidationError('Enter a valid phone number.')
        return phone

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password and len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters.')
        if password and password.isdigit():
            raise forms.ValidationError('Password cannot be entirely numeric.')
        return password


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)