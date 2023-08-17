from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    """
    This model includes additional fields for the user's name and phone number.
    It also maintains many-to-many relationships with Group and Permission.
    """
    # Additional field for user's name
    name = models.CharField(max_length=100)
    # Email field with uniqueness constraint
    email = models.EmailField(unique=True)
    # Field for user's phone number (optional)
    phone = models.CharField(max_length=20, blank=True)

    # Many-to-many relationships with Group and Permission models
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="custom_user_groups"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="custom_user_permissions"
    )

    def __str__(self):
        """
        Returns the username as the string representation of the user.
        """
        return self.username
