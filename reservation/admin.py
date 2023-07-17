from django.contrib import admin
from .models import Reservation

# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'number_of_guests', 'date', 'time', 'is_cancelled']
    list_filter = ['is_cancelled']
    search_fields = ['name', 'email', 'phone']






