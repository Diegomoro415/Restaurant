from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.CharField(max_length=20)
    message = models.TextField()

    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
