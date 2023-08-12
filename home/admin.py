from django.contrib import admin
from .models import UserReview
from .forms import UserReviewForm


# Register your models here.


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('author',)}
    list_filter = ('author', 'created_on', 'approved')
    summernote_fields = ('comment')
    form = UserReviewForm
    list_display = ('author', 'rating', 'created_on', 'approved')
    search_fields = ('author', 'created_on')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} review has been approved.")


