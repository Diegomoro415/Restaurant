from django.shortcuts import render

# Create your views here.

def contact_us_view(request):
    return render(request, 'Contact_us/contact_us.html')

def handler404(request, exception=None):
    return render(request, 'errors/404.html', status=404)

def handler403(request, exception=None):
    return render(request, 'errors/403.html', status=403)

def handler500(request):
    return render(request, 'errors/500.html', status=500)