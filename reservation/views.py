from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Reservation


# Create your views here.
@login_required
def reservation_view(request):
    if request.method == 'POST':
        user = request.user
        phone = request.POST['phone']
        number_of_guests = request.POST['number-guests']
        date_str = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']

        # Converting the date format (DD/MM/YYYY)
        date = datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        # Create the reservation with the authenticated user's data
        reservation = Reservation(
            user=user,
            name=user.username,
            email=user.email,
            phone=phone,
            number_of_guests=number_of_guests,
            date=date,
            time=time,
            message=message
        )
        reservation.save()

        return redirect('reservation:reservation_detail', reservation_id=reservation.id)

    else:
        # Check if the user already has an open reservation
        existing_reservation = Reservation.objects.filter(user=request.user, is_cancelled=False).first()

        if existing_reservation:
            # If it already has an open reservation, display the reservation information on the page
            return render(request, 'Reservation/reservation_options.html', {'reservation': existing_reservation})
        else:
        # If it doesn't have an open reservation, display the reservation form normally
            return render(request, 'Reservation/reservation.html')

def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.is_cancelled = True
        reservation.save()
        return redirect('reservation:reservation')

    return redirect('reservation:reservation')


def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'Reservation/reservation_detail.html', {'reservation': reservation})

@login_required
def reservation_options_view(request):
    user = request.user
    reservation_in_progress = Reservation.objects.filter(user=user, is_cancelled=False).first()
    return render(request, 'Reservation/reservation_options.html', {'reservation_in_progress': reservation_in_progress})