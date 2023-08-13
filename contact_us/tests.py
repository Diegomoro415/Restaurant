from django.test import TestCase
from django.urls import reverse

class ContactUsViewTests(TestCase):
    """
    Test suite for the 'contact_us' view.
    """

    def test_contact_us_view(self):
        """
        Test if the 'contact_us' view returns a 200 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('contact_us:contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Contact_us/contact_us.html')

class ErrorHandlingTests(TestCase):
    """
    Test suite for custom error handling views.
    """

    def test_404_handler(self):
        """
        Test if the custom 404 error handler returns a 404 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('contact_us:handler404'))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')

    def test_403_handler(self):
        """
        Test if the custom 403 error handler returns a 403 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('contact_us:handler403'))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

    def test_500_handler(self):
        """
        Test if the custom 500 error handler returns a 500 status code
        and uses the correct template.
        """
        response = self.client.get(reverse('contact_us:handler500'))
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'errors/500.html')
