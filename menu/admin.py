from django.contrib import admin
from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Menu model.

    This class defines customizations for the
    admin interface of the Menu model,
    including displayed columns, filters,
    search fields, and default sorting order.
    """

    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    ordering = ('name',)
