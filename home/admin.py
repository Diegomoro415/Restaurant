from django.contrib import admin
from .models import UserReview
from .forms import UserReviewForm

# Register your models here.

@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserReview model.
    """
    # Prepopulate the 'slug' field based on the 'author' field
    prepopulated_fields = {'slug': ('author',)}
    
    # Add filters for author, creation date, and approval status
    list_filter = ('author', 'created_on', 'approved')
    
    # Use Summernote for the 'comment' field in the admin
    summernote_fields = ('comment',)
    
    # Use the custom UserReviewForm for admin form
    form = UserReviewForm
    
    # Display author, rating, creation date, and approval status in the list view
    list_display = ('author', 'rating', 'created_on', 'approved')
    
    # Enable searching by author and creation date
    search_fields = ('author', 'created_on')
    
    # Define a custom action to approve selected reviews
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        """
        Custom action to approve selected reviews.

        :param request: The HTTP request object.
        :param queryset: A queryset of UserReview objects to be approved.
        """
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} review(s) have been approved.")