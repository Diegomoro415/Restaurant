from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from menu.admin import MenuAdmin
from menu.models import Menu


class MockRequest:
    """A mock class representing an HTTP request."""


class MockSuperUser:
    """
    A mock class representing a superuser with permission checking.

    This mock class is used to simulate a superuser
    with permission checks in tests.
    """

    def has_perm(self, perm):
        """
        Simulate checking if a superuser has a specific permission.

        :param perm: The permission to check.
        :return: True, indicating that the superuser has the permission.
        """
        return True


class MenuAdminTest(TestCase):
    def setUp(self):
        """
        Set up a mock AdminSite and MenuAdmin instance for testing.

        This method is run before each test method to
        create the necessary instances.
        """
        self.site = AdminSite()
        self.menu_admin = MenuAdmin(Menu, self.site)

    def test_list_display(self):
        """Test the list_display attribute of MenuAdmin."""
        self.assertEqual(
            list(self.menu_admin.list_display),
            ['name', 'category', 'price']
        )

    def test_list_filter(self):
        """Test the list_filter attribute of MenuAdmin."""
        self.assertEqual(
            list(self.menu_admin.list_filter),
            ['category']
        )

    def test_search_fields(self):
        """Test the search_fields attribute of MenuAdmin."""
        self.assertEqual(
            list(self.menu_admin.search_fields),
            ['name', 'category']
        )

    def test_ordering(self):
        """Test the ordering attribute of MenuAdmin."""
        self.assertEqual(
            self.menu_admin.ordering,
            ('name',)
        )

    def test_has_add_permission(self):
        """Test that a superuser has add permission in MenuAdmin."""
        request = MockRequest()
        request.user = MockSuperUser()
        self.assertTrue(self.menu_admin.has_add_permission(request))

    def test_has_change_permission(self):
        """Test that a superuser has change permission in MenuAdmin."""
        request = MockRequest()
        request.user = MockSuperUser()
        self.assertTrue(self.menu_admin.has_change_permission(request))

    def test_has_delete_permission(self):
        """Test that a superuser has delete permission in MenuAdmin."""
        request = MockRequest()
        request.user = MockSuperUser()
        self.assertTrue(self.menu_admin.has_delete_permission(request))
