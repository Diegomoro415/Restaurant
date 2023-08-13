from django.test import TestCase
from accounts.models import CustomUser
from django.contrib.auth.models import Group, Permission

class CustomUserTestCase(TestCase):
    """
    Test suite for the CustomUser model.
    """

    def setUp(self):
        """
        Set up the test environment by creating a test user.
        """
        # Create a test user for each test method
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            name='Test User',
            phone='1234567890'
        )

    def test_user_creation(self):
        """
        Test if the user is created correctly with expected fields.
        """
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.phone, '1234567890')

    def test_user_str_representation(self):
        """
        Test if the __str__ representation of the user is correct.
        """
        self.assertEqual(str(self.user), 'testuser')

    def test_user_groups_and_permissions(self):
        """
        Test user's group and permission associations.
        """
        # Create a test group
        group = Group.objects.create(name='Test Group')
        # Add the test group to the user's groups
        self.user.groups.add(group)
        # Check if the user is in the test group
        self.assertIn(group, self.user.groups.all())

        # Get a test permission (change this to match your actual permission)
        permission = Permission.objects.get(codename='add_customuser')
        # Add the test permission to the user's user_permissions
        self.user.user_permissions.add(permission)
        # Check if the user has the test permission
        self.assertIn(permission, self.user.user_permissions.all())
