from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menu.views import menu_list, menu_detail


class TestUrls(SimpleTestCase):

    def test_menu_list_url_resolves(self):
        # Test that the 'menu' URL resolves to the 'menu_list' view function
        url = reverse('menu:menu')
        self.assertEqual(resolve(url).func, menu_list)

    def test_menu_detail_url_resolves(self):
        # Test that the 'menu_detail' URL with a sample slug
        # resolves to the 'menu_detail' view function
        url = reverse('menu:menu_detail', args=['sample-slug'])
        self.assertEqual(resolve(url).func, menu_detail)
