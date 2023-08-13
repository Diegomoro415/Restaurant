from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)  # Additional field for user's name
    email = models.EmailField(unique=True)  # Email field with uniqueness constraint
    phone = models.CharField(max_length=20, blank=True)  # Field for user's phone number (optional)

    # Many-to-many relationships with Group and Permission models
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="custom_user_groups"  # Reverse relation for groups
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="custom_user_permissions"  # Reverse relation for permissions
    )

    def __str__(self):
        return self.username  # Return the username as the string representation
