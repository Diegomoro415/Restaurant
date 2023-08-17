from django.contrib import admin
from django.test import TestCase
from reservation.admin import ReservationAdmin
from reservation.models import Reservation


class ReservationAdminTest(TestCase):
    def test_reservation_admin_should_be_registered(self):
        """
        Test that the ReservationAdmin is registered with the admin site.
        """
        self.assertTrue(isinstance(
            admin.site._registry[Reservation], ReservationAdmin))

    def test_reservation_admin_list_display(self):
        """
        Test that the list_display attribute of
        ReservationAdmin is as expected.
        """
        expected = [
            'name',
            'email',
            'phone',
            'number_of_guests',
            'date',
            'time',
            'is_cancelled']
        self.assertEqual(
            ReservationAdmin.list_display, expected)

    def test_reservation_admin_list_filter(self):
        """
        Test that the list_filter attribute of ReservationAdmin is as expected.
        """
        expected = ['is_cancelled']
        self.assertEqual(ReservationAdmin.list_filter, expected)

    def test_reservation_admin_search_fields(self):
        """
        Test that the search_fields attribute of
        ReservationAdmin is as expected.
        """
        expected = ['name', 'email', 'phone']
        self.assertEqual(ReservationAdmin.search_fields, expected)
