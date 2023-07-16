from django.shortcuts import render

# Create your views here.

def reservation_view(request):
    return render(request, 'Reservation/reservation.html')