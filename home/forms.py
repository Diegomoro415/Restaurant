from django import forms
from .models import UserReview


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['comment', 'rating']
        exclude = ['author']
