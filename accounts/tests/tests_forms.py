from django.test import TestCase
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from accounts.forms import UserLoginForm, UserRegistrationForm

class UserFormsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        
    def test_user_login_form_valid(self):
        # Create a user login form instance with valid data
        form = UserLoginForm(data={'username': 'testuser', 'password': 'testpassword'})
        self.assertTrue(form.is_valid())

    def test_user_login_form_invalid(self):
        # Create a user login form instance with invalid data
        form = UserLoginForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())

    def test_user_registration_form_valid(self):
        # Create a user registration form instance with valid data
        form = UserRegistrationForm(data={'username': 'newuser', 'email': 'newuser@example.com', 'password1': 'newpassword', 'password2': 'newpassword'})
        self.assertTrue(form.is_valid())

    def test_user_registration_form_invalid(self):
        # Create a user registration form instance with invalid data
        form = UserRegistrationForm(data={'username': '', 'email': 'invalidemail', 'password1': 'password', 'password2': 'mismatchedpassword'})
        self.assertFalse(form.is_valid())
