from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class UserReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                default=1)
    comment = models.TextField()
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    class Meta:
        ordering =['-created_on']

    def __str__(self):
        return f"Review by {self.author} - Rating: {self.rating}"