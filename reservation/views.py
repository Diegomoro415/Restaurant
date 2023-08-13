from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Reservation

@login_required
def reservation_view(request):
    """
    View to handle creating a new reservation or displaying an existing open reservation.

    If the user has an existing open reservation, display its information.
    If not, display the reservation form for creating a new reservation.
    """
    if request.method == 'POST':
        # Extract reservation details from the form
        user = request.user
        phone = request.POST['phone']
        number_of_guests = request.POST['number-guests']
        date_str = request.POST['date']
        time = request.POST['time']
        message = request.POST['message']

        # Convert the date format (DD/MM/YYYY) to (YYYY-MM-DD)
        date = datetime.strptime(date_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        # Create and save the reservation
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
            # If an open reservation exists, display its information
            return render(request, 'Reservation/reservation_options.html', {'reservation': existing_reservation})
        else:
            # If no open reservation, display the reservation form
            return render(request, 'Reservation/reservation.html')

def cancel_reservation(request, reservation_id):
    """
    View to handle canceling a reservation.

    When a POST request is received, mark the reservation as cancelled and redirect to reservation view.
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        reservation.is_cancelled = True
        reservation.save()
        return redirect('reservation:reservation')

    return redirect('reservation:reservation')

def reservation_detail(request, reservation_id):
    """
    View to display details of a specific reservation.
    """
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'Reservation/reservation_detail.html', {'reservation': reservation})

@login_required
def reservation_options_view(request):
    """
    View to display options for an existing reservation in progress.
    """
    user = request.user
    reservation_in_progress = Reservation.objects.filter(user=user, is_cancelled=False).first()
    return render(request, 'Reservation/reservation_options.html', {'reservation_in_progress': reservation_in_progress})
