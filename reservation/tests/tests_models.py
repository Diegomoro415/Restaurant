from django.test import TestCase
from django.contrib.auth.models import User
from reservation.models import Reservation

class ReservationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a test user and a reservation for testing
        user = User.objects.create_user(username='testuser', password='testpass')
        Reservation.objects.create(
            user=user,
            name='John Doe',
            email='johndoe@example.com',
            phone='123-456-7890',
            number_of_guests=4,
            date='2023-08-15',
            time='18:00',
            message='Test reservation message'
        )

    def test_reservation_user(self):
        # Test that the reservation's user is as expected
        reservation = Reservation.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(reservation.user, user)

    def test_reservation_name(self):
        # Test that the reservation's name is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.name, 'John Doe')

    def test_reservation_email(self):
        # Test that the reservation's email is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.email, 'johndoe@example.com')

    def test_reservation_phone(self):
        # Test that the reservation's phone is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.phone, '123-456-7890')

    def test_reservation_number_of_guests(self):
        # Test that the reservation's number of guests is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.number_of_guests, 4)

    def test_reservation_date(self):
        # Test that the reservation's date is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(str(reservation.date), '2023-08-15')

    def test_reservation_time(self):
        # Test that the reservation's time is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.time, '18:00')

    def test_reservation_message(self):
        # Test that the reservation's message is as expected
        reservation = Reservation.objects.get(id=1)
        self.assertEqual(reservation.message, 'Test reservation message')

    def test_reservation_is_cancelled(self):
        # Test that the reservation's 'is_cancelled' field is False by default
        reservation = Reservation.objects.get(id=1)
        self.assertFalse(reservation.is_cancelled)
