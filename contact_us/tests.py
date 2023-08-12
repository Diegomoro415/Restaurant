from django.test import TestCase
from django.urls import reverse

class ContactUsViewTests(TestCase):
    def test_contact_us_view(self):
        response = self.client.get(reverse('contact_us:contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Contact_us/contact_us.html')

class ErrorHandlingTests(TestCase):
    def test_404_handler(self):
        response = self.client.get(reverse('contact_us:handler404'))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')

    def test_403_handler(self):
        response = self.client.get(reverse('contact_us:handler403'))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_500_handler(self):
        response = self.client.get(reverse('contact_us:handler500'))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'errors/500.html')