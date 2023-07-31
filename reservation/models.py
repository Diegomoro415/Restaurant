from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    message = models.TextField()

    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation {self.id} - {self.name}"
