from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
