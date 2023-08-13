from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import (
    reservation_view,
    reservation_options_view,
    cancel_reservation,
    reservation_detail,
)

class TestUrls(SimpleTestCase):

    def test_reservation_url_resolves(self):
        """
        Test if the empty URL ('reservation') resolves to the 'reservation_view' function.
        """
        url = reverse('reservation:reservation')
        self.assertEqual(resolve(url).func, reservation_view)

    def test_reservation_options_url_resolves(self):
        """
        Test if the 'reservation_options/' URL resolves to the 'reservation_options_view' function.
        """
        url = reverse('reservation:reservation_options')
        self.assertEqual(resolve(url).func, reservation_options_view)

    def test_cancel_reservation_url_resolves(self):
        """
        Test if the 'cancel/<int:reservation_id>/' URL resolves to the 'cancel_reservation' function.
        """
        url = reverse('reservation:cancel_reservation', args=[1])  # Change 1 to a valid reservation ID
        self.assertEqual(resolve(url).func, cancel_reservation)

    def test_reservation_detail_url_resolves(self):
        """
        Test if the 'detail/<int:reservation_id>/' URL resolves to the 'reservation_detail' function.
        """
        url = reverse('reservation:reservation_detail', args=[1])  # Change 1 to a valid reservation ID
        self.assertEqual(resolve(url).func, reservation_detail)
