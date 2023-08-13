from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from menu.models import Menu
from django.urls import reverse

class MenuViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for menu image testing.

        This method is run once to create a test image file for menu image testing.
        """
        cls.test_image = SimpleUploadedFile(
            name='ut_logo.png',
            content=open('static/site_static/images/ut_logo.png', 'rb').read(),
            content_type='image/png'
        )

    def test_menu_list_view(self):
        """
        Test rendering of the menu list view.

        This test checks if the menu list view is rendered successfully and uses the correct template.
        """
        url = reverse('menu:menu')  # Assuming your app_name is 'menu'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Expecting successful response
        self.assertTemplateUsed(response, 'Menu/list.html')  # Expecting the correct template

    def test_menu_detail_view(self):
        """
        Test rendering of the menu detail view.

        This test checks if the menu detail view is rendered successfully and uses the correct template.
        """
        menu = Menu.objects.create(
            category='Category',
            name='Test Menu',
            description='Test Description',
            price=9.99,
            image=self.test_image,
        )
        url = reverse('menu:menu_detail', kwargs={'slug': menu.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Expecting successful response
        self.assertTemplateUsed(response, 'menu/detail.html')  # Expecting the correct template
