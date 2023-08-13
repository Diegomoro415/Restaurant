from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    """
    Model representing a reservation made by a user.
    """

    # A foreign key relationship to the User model, representing the user who made the reservation.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # The name associated with the reservation.
    name = models.CharField(max_length=255)

    # The email address of the user who made the reservation.
    email = models.EmailField()

    # The phone number associated with the reservation.
    phone = models.CharField(max_length=20)

    # The number of guests for the reservation.
    number_of_guests = models.IntegerField()

    # The date of the reservation.
    date = models.DateField()

    # The time of the reservation.
    time = models.CharField(max_length=20)

    # An optional message or note associated with the reservation.
    message = models.TextField()

    # A boolean field indicating whether the reservation has been cancelled.
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        """
        Return a string representation of the reservation, including its ID and name.
        """
        return f"Reservation {self.id} - {self.name}"
