from django.contrib import admin
from .models import Menu

# Register the Menu model with the admin site using a decorator
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    # Customize the displayed columns in the list view of the admin
    list_display = ('name', 'category', 'price')
    
    # Add a filter sidebar to filter by category
    list_filter = ('category',)
    
    # Add search fields for name and category
    search_fields = ('name', 'category')
    
    # Define the default sorting order for the list view
    ordering = ('name',)
