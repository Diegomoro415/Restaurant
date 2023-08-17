from django.db import models
from django.contrib.auth.models import User


# Define choices for the status of a UserReview
STATUS = ((0, "Draft"), (1, "Published"))


class UserReview(models.Model):
    """
    Represents a user review for your application.
    """
    # Define a foreign key relationship with
    # the User model for the review's author
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Author")

    # Field to store the review comment
    comment = models.TextField(max_length=500, verbose_name="Comment")

    # Field to store the rating given by the user
    rating = models.IntegerField(
        choices=((1, '1'),
                 (2, '2'),
                 (3, '3'),
                 (4, '4'),
                 (5, '5')), verbose_name="Rating"
                )

    # Automatically set the creation date and time
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created On"
    )

    # Field to indicate whether the review has been approved
    approved = models.BooleanField(
        default=False,
        verbose_name="Approved"
    )

    # Field to indicate the status of the review (Draft or Published)
    status = models.IntegerField(
        choices=STATUS,
        default=0,
        verbose_name="Status"
    )

    # Field to store a unique slug for the review (used for URLs)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True,
        verbose_name="Slug"
    )

    class Meta:
        # Define the default ordering
        # of UserReview instances by creation date
        ordering = ['-created_on']
        verbose_name_plural = "User Reviews"

    def __str__(self):
        """
        Return a human-readable string representation
        of the UserReview instance.
        """
        return f"Review by {self.author} - Rating: {self.rating}"
