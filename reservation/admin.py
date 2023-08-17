from django.contrib import admin
from .models import Reservation


# Register the Reservation model with the admin site using a decorator
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Custom admin interface configuration for the Reservation model.
    """
    # The fields displayed in the list view of the admin interface.
    list_display = [
        'name',
        'email',
        'phone',
        'number_of_guests',
        'date',
        'time',
        'is_cancelled']
    # The filters displayed in the right sidebar of the admin list view.
    list_filter = ['is_cancelled']
    # The fields available for searching in the admin interface.
    search_fields = ['name', 'email', 'phone']
