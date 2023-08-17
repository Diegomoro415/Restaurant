from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


# Custom login form
class UserLoginForm(AuthenticationForm):
    """
    Custom login form based on Django's AuthenticationForm.
    """
    class Meta:
        fields = ('username', 'password')  # Define the fields for the form


# Custom registration
class UserRegistrationForm(forms.ModelForm):
    """
    Custom registration form using Django's ModelForm.
    """

    class Meta:
        model = get_user_model()  # Use the user model specified in settings
        fields = ('username', 'email')  # Define the fields for the form
