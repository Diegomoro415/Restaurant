from django import forms
from .models import UserReview

# Define a form for creating/editing UserReview instances
class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['comment', 'rating']
        exclude = ['author']
