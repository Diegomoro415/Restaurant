from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class AccountsUrlsTestCase(TestCase):
    def test_register_url(self):
        url = reverse('accounts:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Accounts/register.html')

    def test_login_url(self):
        url = reverse('accounts:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Accounts/login.html')

    def test_logout_url(self):
        url = reverse('accounts:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirects to login page
