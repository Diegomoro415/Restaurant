from django.shortcuts import render

# Create your views here.

def contact_us_view(request):
    return render(request, 'Contact_us/contact_us.html')
