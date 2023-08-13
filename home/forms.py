from django import forms
from .models import UserReview

class UserReviewForm(forms.ModelForm):
    """
    A form for creating/editing UserReview instances.
    """
    class Meta:
        model = UserReview
        fields = ['comment', 'rating']
        exclude = ['author']
