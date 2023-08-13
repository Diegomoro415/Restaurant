from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.admin import AdminSite
from django.urls import reverse
from accounts.admin import CustomUserAdmin
from accounts.models import CustomUser

class CustomUserAdminTest(TestCase):
    """
    Test suite for the CustomUserAdmin class in the admin panel.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a custom admin site
        self.admin_site = AdminSite()
        # Create an instance of the CustomUserAdmin using the custom admin site
        self.user_admin = CustomUserAdmin(CustomUser, self.admin_site)
        self.client = Client()

    def test_admin_page_access(self):
        """
        Test accessing the admin change list page for the CustomUser model.
        """
        # Create a superuser for testing
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='admin', password='password', email='admin@example.com')
        # Log in the admin user and access the change list page for CustomUser model
        self.client.force_login(admin_user)
        url = reverse('admin:accounts_customuser_changelist')
        response = self.client.get(url)
        # Verify that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_admin_list_display(self):
        """
        Test the list display of fields in CustomUserAdmin.
        """
        # Verify that required fields are present in the list display of CustomUserAdmin
        self.assertIn('username', self.user_admin.list_display)
        self.assertIn('email', self.user_admin.list_display)
        self.assertIn('first_name', self.user_admin.list_display)
        self.assertIn('last_name', self.user_admin.list_display)
        self.assertIn('is_staff', self.user_admin.list_display)
