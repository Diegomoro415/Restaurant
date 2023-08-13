from django.test import TestCase
from menu.models import Menu

class MenuModelTest(TestCase):

    def setUp(self):
        """
        Set up a test Menu instance for model testing.

        This method is run before each test method to create the necessary instances.
        """
        self.menu = Menu.objects.create(
            category='Appetizer',
            name='Crispy Fried Chicken',
            description='Delicious fried chicken with crispy crust.',
            price=9.99,
            image='menu/crispy-fried-chicken.jpg',
            slug='crispy-fried-chicken'
        )

    def test_menu_model_str(self):
        """
        Test the string representation of the Menu model.

        This test ensures that the __str__ method of the Menu model returns the expected string.
        """
        self.assertEqual(str(self.menu), 'Crispy Fried Chicken')

    def test_menu_model_slug(self):
        """
        Test that the slug field was set correctly in the Menu model.

        This test checks that the 'slug' field of the Menu model was set correctly during instance creation.
        """
        self.assertEqual(self.menu.slug, 'crispy-fried-chicken')

    def test_menu_model_verbose_name(self):
        """
        Test the verbose name of the Menu model.

        This test checks that the verbose name of the Menu model matches the expected value.
        """
        self.assertEqual(Menu._meta.verbose_name, 'menu')

    def test_menu_model_verbose_name_plural(self):
        """
        Test the verbose plural name of the Menu model.

        This test checks that the verbose plural name of the Menu model matches the expected value.
        """
        self.assertEqual(Menu._meta.verbose_name_plural, 'menu')

    # Add more tests here as needed

    def tearDown(self):
        """
        Clean up by deleting the test Menu instance.

        This method is run after each test method to delete the test Menu instance.
        """
        self.menu.delete()
