from django.test import TestCase
from menu.models import Menu

class MenuModelTest(TestCase):

    def setUp(self):
        # Create a test Menu instance
        self.menu = Menu.objects.create(
            category='Appetizer',
            name='Crispy Fried Chicken',
            description='Delicious fried chicken with crispy crust.',
            price=9.99,
            image='menu/crispy-fried-chicken.jpg',
            slug='crispy-fried-chicken'
        )

    def test_menu_model_str(self):
        # Test the string representation of the Menu model
        self.assertEqual(str(self.menu), 'Crispy Fried Chicken')

    def test_menu_model_slug(self):
        # Test that the slug field was set correctly
        self.assertEqual(self.menu.slug, 'crispy-fried-chicken')

    def test_menu_model_verbose_name(self):
        # Test the verbose name of the Menu model
        self.assertEqual(Menu._meta.verbose_name, 'menu')

    def test_menu_model_verbose_name_plural(self):
        # Test the verbose plural name of the Menu model
        self.assertEqual(Menu._meta.verbose_name_plural, 'menu')

    # Add more tests here as needed

    def tearDown(self):
        # Clean up by deleting the test Menu instance
        self.menu.delete()
