from django.test import TestCase
from home.models import UserReview
from django.contrib.auth.models import User

class UserReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        author = User.objects.create_user(username='testuser', password='12345')
        UserReview.objects.create(
            author=author,
            comment='This is a test comment',
            rating=5,
            approved=True,
            status=1,
            slug='test-slug'
        )

    def test_comment_max_length(self):
        # Test that the maximum length of the 'comment' field is as expected
        review = UserReview.objects.get(id=1)
        max_length = review._meta.get_field('comment').max_length
        self.assertEqual(max_length, 500)

    def test_rating_choices(self):
        # Test that the 'rating' field choices match the expected values
        review = UserReview.objects.get(id=1)
        choices = list(review._meta.get_field('rating').choices)
        expected_choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
        self.assertEqual(choices, expected_choices)

    def test_approved_default_value(self):
        # Test that the 'approved' field has the default value of True
        review = UserReview.objects.get(id=1)
        self.assertTrue(review.approved)

    def test_status_default_value(self):
        # Test that the 'status' field has the default value of 1
        review = UserReview.objects.get(id=1)
        self.assertEqual(review.status, 1)

    def test_slug_unique(self):
        # Test that the 'slug' field is set as unique
        review = UserReview.objects.get(id=1)
        field = review._meta.get_field('slug')
        self.assertTrue(field.unique)

    def test_ordering(self):
        # Test that the default ordering for UserReview model is as expected
        self.assertEqual(UserReview.objects.get(id=1)._meta.ordering, ['-created_on'])

    def test_str_method(self):
        # Test the string representation of the UserReview model
        review = UserReview.objects.get(id=1)
        expected_str = f"Review by {review.author} - Rating: {review.rating}"
        self.assertEqual(str(review), expected_str)
