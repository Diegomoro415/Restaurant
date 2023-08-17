from django.test import TestCase
from django.urls import reverse, resolve
from home import views


class HomeAppUrlsTest(TestCase):
    def test_home_url_resolves(self):
        # Test that the 'home' URL
        # resolves to the 'home_view' function in 'views.py'
        url = reverse('home:home')
        self.assertEqual(resolve(url).func, views.home_view)

    def test_home_view_url_resolves(self):
        # Test that the 'home_view' URL
        # resolves to the 'home_view' function in 'views.py'
        url = reverse('home:home_view')
        self.assertEqual(resolve(url).func, views.home_view)

    def test_user_reviews_url_resolves(self):
        # Test that the 'user_reviews' URL
        # resolves to the 'user_reviews' function in 'views.py'
        url = reverse('home:user_reviews')
        self.assertEqual(resolve(url).func, views.user_reviews)

    def test_create_review_url_resolves(self):
        # Test that the 'create_review' URL
        # resolves to the 'create_review' function in 'views.py'
        url = reverse('home:create_review')
        self.assertEqual(resolve(url).func, views.create_review)

    def test_edit_review_url_resolves(self):
        # Test that the 'edit_review' URL with a review ID
        # resolves to the 'edit_review' function in 'views.py'
        url = reverse(
            'home:edit_review',
            args=[1]
        )  # Change 1 to a valid review ID
        self.assertEqual(resolve(url).func, views.edit_review)

    def test_delete_review_url_resolves(self):
        # Test that the 'delete_review' URL with a review ID
        # resolves to the 'delete_review' function in 'views.py'
        url = reverse(
            'home:delete_review',
            args=[1]
        )  # Change 1 to a valid review ID
        self.assertEqual(resolve(url).func, views.delete_review)
