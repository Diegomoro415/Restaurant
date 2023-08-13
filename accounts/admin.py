from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define the new Custom User model
class CustomUserAdmin(UserAdmin):
    """
    This configuration customizes how the CustomUser model is displayed
    and managed in the Django admin panel.
    """
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    """
    List of fields to be displayed in the list view of CustomUser instances
    in the admin panel.
    """

# Update the registration of the Custom User model in the admin panel
admin.site.register(CustomUser, CustomUserAdmin)
"""
Registers the CustomUser model with the CustomUserAdmin configuration
to manage and display CustomUser instances in the admin panel.
"""