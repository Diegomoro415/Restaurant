from django.shortcuts import render, get_object_or_404
from .models import Menu

def menu_list(request):
    """
    View to list menu items and categorize them.

    :param request: The HTTP request object.
    :return: Rendered HTML template with menu items and categories.
    """
    # Retrieve all menu items from the database
    menu_list = Menu.objects.all()
    
    # Create a set of unique categories from the menu items
    categories = set(menu.category for menu in menu_list)
    
    # Define the context data to be passed to the template
    context = {'menu_list': menu_list, 'categories': categories}
    
    # Render the 'list.html' template with the provided context
    return render(request, 'Menu/list.html', context)

def menu_detail(request, slug):
    """
    View to display details of a specific menu item.

    :param request: The HTTP request object.
    :param slug: The slug of the menu item.
    :return: Rendered HTML template with menu item details.
    """
    # Retrieve the menu item with the specified slug from the database
    menu_detail = get_object_or_404(Menu, slug=slug)
    
    # Define the context data to be passed to the template
    context = {'menu_detail': menu_detail}
    
    # Render the 'detail.html' template with the provided context
    return render(request, 'menu/detail.html', context)
