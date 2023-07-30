from django import forms
from .models import SuggestedDish, UserReview


class SuggestedDishForm(forms.ModelForm):
    class Meta:
        model = SuggestedDish
        fields = ['name', 'description', 'image', 'price']

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['comment', 'rating']
        exclude = ['author']
