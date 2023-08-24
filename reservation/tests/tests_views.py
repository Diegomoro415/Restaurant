from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from reservation.models import Reservation


class ReservationViewsTest(TestCase):
    def setUp(self):
        # Create a test client and user,
        # and set up a reservation for testing
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.reservation = Reservation.objects.create(
            user=self.user,
            name=self.user.username,
            email=self.user.email,
            phone='1234567890',
            number_of_guests=4,
            date=datetime.now().date(),
            time='18:00',
            message='Test reservation',
    )

    def test_reservation_view_GET(self):
        """
        Test GET request to 'reservation' view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('reservation:reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Reservation/reservation_options.html')

    def test_reservation_view_POST(self):
        """
        Test POST request to 'reservation' view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('reservation:reservation'), {
            'phone': '9876543210',
            'number-guests': 3,
            'date': '15/08/2023',
            'time': '19:00',
            'message': 'New test reservation',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Reservation.objects.filter(
            phone='9876543210').exists())

    def test_reservation_options_view(self):
        """
        Test GET request to 'reservation_options' view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('reservation:reservation_options'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'Reservation/reservation_options.html')

    def test_cancel_reservation(self):
        """
        Test cancellation of a reservation.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse(
            'reservation:cancel_reservation',
            kwargs={'reservation_id': self.reservation.id}))
        self.assertEqual(response.status_code, 302)
        self.reservation.refresh_from_db()
        self.assertTrue(self.reservation.is_cancelled)

    def test_reservation_detail_view(self):
        """
        Test GET request to 'reservation_detail' view.
        """
        self.client.login(username='testuser',
                          password='testpassword')
        response = self.client.get(reverse(
            'reservation:reservation_detail',
            args=[self.reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'Reservation/reservation_detail.html')
