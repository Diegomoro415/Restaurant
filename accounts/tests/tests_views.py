from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsViewsTestCase(TestCase):
    """
    Test case for testing views in the 'accounts' app.
    """

    def setUp(self):
        """
        Set up the test case by initializing the test client and URLs.
        """
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.register_url = reverse('accounts:register')
        self.logout_url = reverse('accounts:logout')

    def test_login_view(self):
        """
        Test the login view to ensure it returns the
        correct status code and template.
        """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Accounts/login.html')

    def test_register_view(self):
        """
        Test the register view to ensure it returns the
        correct status code and template.
        """
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Accounts/register.html')

    def test_logout_view(self):
        """
        Test the logout view by creating a test user, logging them in,
        and checking that the view redirects after logout.
        """
        # Create a test user
        user = User.objects.create_user(username='testuser',
                                        password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
