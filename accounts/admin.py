from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Define the new Custom User model
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Update the registration of the Custom User model in the admin panel
admin.site.register(CustomUser, CustomUserAdmin)
