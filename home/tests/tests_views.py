from django.test import TestCase
from django.urls import reverse
from home.models import UserReview
from django.contrib.auth.models import User


class HomeAppViewsTest(TestCase):

    def setUp(self):
        """
        Set up non-modified objects used by all test methods.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.review = UserReview.objects.create(
            author=self.user,
            comment='Test comment',
            rating=4,
        )

    def test_home_view_GET(self):
        """
        Test GET request to 'home_view' and check
        response status code and template used.
        """
        response = self.client.get(reverse('home:home_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home/home.html')

    def test_home_view_POST_authenticated(self):
        """
        Test POST request to 'home_view' when authenticated,
        check response status code and redirection.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('home:home_view'), {
            'comment': 'This is a test comment',
            'rating': 5,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home_view'))

    def test_home_view_POST_not_authenticated(self):
        """
        Test POST request to 'home_view' when not authenticated,
        check response status code and redirection.
        """
        response = self.client.post(reverse('home:home_view'), {
            'comment': 'This is a test comment',
            'rating': 5,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_create_review_POST_authenticated(self):
        """
        Test POST request to 'create_review' when authenticated,
        check response status code and redirection.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('home:create_review'), {
            'comment': 'This is a test comment',
            'rating': 5,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home_view'))

    def test_create_review_GET(self):
        """
        Test GET request to 'create_review',
        expecting redirection to login page.
        """
        response = self.client.get(reverse('home:create_review'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse('login') + '?next=' + reverse('home:create_review'))

    def test_edit_review_POST_authenticated(self):
        """
        Test POST request to 'edit_review' when authenticated,
        check response status code and redirection.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse(
            'home:edit_review', args=[self.review.pk]), {
            'comment': 'Updated test comment',
            'rating': 3,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home_view'))

    def test_edit_review_GET(self):
        """
        Test GET request to 'edit_review',
        check response status code and template used.
        """
        response = self.client.get(reverse(
            'home:edit_review', args=[self.review.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home/edit_review.html')

    def test_delete_review_POST_authenticated(self):
        """
        Test POST request to 'delete_review' when authenticated,
        check response status code and redirection.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse(
            'home:delete_review', args=[self.review.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home_view'))

    def test_delete_review_GET(self):
        """
        Test GET request to 'delete_review',
        check response status code and template used.
        """
        response = self.client.get(reverse(
            'home:delete_review', args=[self.review.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home/home.html')
