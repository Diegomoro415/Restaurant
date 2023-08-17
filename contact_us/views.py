from django.shortcuts import render


# View function for the Contact Us page
def contact_us_view(request):
    """
    Renders the Contact Us page.

    :param request: The HTTP request object.
    :return: Rendered HTML template for the Contact Us page.
    """
    return render(request, 'Contact_us/contact_us.html')


# Custom error handler for 404 Not Found errors
def handler404(request, exception=None):
    """
    Renders the custom 404 Not Found error page.

    :param request: The HTTP request object.
    :param exception: The exception that triggered the error (not used here).
    :return: Rendered HTML template for the
    custom 404 error page with a 404 status code.
    """
    return render(request, 'errors/404.html', status=404)


# Custom error handler for 403 Forbidden errors
def handler403(request, exception=None):
    """
    Renders the custom 403 Forbidden error page.

    :param request: The HTTP request object.
    :param exception: The exception that triggered the error (not used here).
    :return: Rendered HTML template for the
    custom 403 error page with a 403 status code.
    """
    return render(request, 'errors/403.html', status=403)


# Custom error handler for 500 Internal Server Error errors
def handler500(request):
    """
    Renders the custom 500 Internal Server Error page.

    :param request: The HTTP request object.
    :return: Rendered HTML template for the
    custom 500 error page with a 500 status code.
    """
    return render(request, 'errors/500.html', status=500)
