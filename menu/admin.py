from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    ordering = ('name',)
