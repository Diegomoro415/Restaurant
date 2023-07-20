from django.contrib import admin
from .models import SuggestedDish, UserReview
from .forms import SuggestedDishForm, UserReviewForm

# Register your models here.

class SuggestedDishAdmin(admin.ModelAdmin):
    form = SuggestedDishForm

class UserReviewAdmin(admin.ModelAdmin):
    form = UserReviewForm

admin.site.register(SuggestedDish, SuggestedDishAdmin)
admin.site.register(UserReview, UserReviewAdmin)
