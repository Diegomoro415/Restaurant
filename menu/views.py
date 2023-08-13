from django.shortcuts import render
from .models import Menu

# View to list menu items and categorize them
def menu_list(request):
    # Retrieve all menu items from the database
    menu_list = Menu.objects.all()
    
    # Create a set of unique categories from the menu items
    categories = set(menu.category for menu in menu_list)
    
    # Define the context data to be passed to the template
    context = {'menu_list': menu_list, 'categories': categories}
    
    # Render the 'list.html' template with the provided context
    return render(request, 'Menu/list.html', context)

# View to display details of a specific menu item
def menu_detail(request, slug):
    # Retrieve the menu item with the specified slug from the database
    menu_detail = Menu.objects.get(slug=slug)
    
    # Define the context data to be passed to the template
    context = {'menu_detail': menu_detail}
    
    # Render the 'detail.html' template with the provided context
    return render(request, 'menu/detail.html', context)
