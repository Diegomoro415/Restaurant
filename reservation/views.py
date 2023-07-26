from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Reservation


# Create your views here.
@login_required
def reservation_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        number_of_guests = request.POST['number-guests']
        date_str = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']

        # # Converting the date format (DD/MM/YYYY)
        date = datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        
        reservation = Reservation(
            name=name,
            email=email,
            phone=phone,
            number_of_guests=number_of_guests,
            date=date,
            time=time,
            message=message
        )
        reservation.save()
        
        return redirect('reservation:reservation_detail', reservation_id=reservation.id)
    
    return render(request, 'Reservation/reservation.html')

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.is_cancelled = True
        reservation.save()
        return redirect('reservation_detail', reservation_id=reservation.id)

    return render(request, 'Reservation/cancel_reservation.html', {'reservation': reservation})

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'Reservation/reservation_detail.html', {'reservation': reservation})