from django.test import TestCase
from home.forms import UserReviewForm
from home.models import UserReview

class UserReviewFormTest(TestCase):
    def test_user_review_form_valid_data(self):
        # Test that UserReviewForm is valid with correct data
        form = UserReviewForm(data={
            'comment': 'This is a test comment',
            'rating': 5,
        })
        self.assertTrue(form.is_valid())

    def test_user_review_form_empty_data(self):
        # Test that UserReviewForm is invalid with empty data
        form = UserReviewForm(data={})
        self.assertFalse(form.is_valid())
        # Expecting two errors as 'comment' and 'rating' are required fields
        self.assertEquals(len(form.errors), 2)
