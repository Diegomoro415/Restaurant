from django.db import models

# Create your models here.
class SuggestedDish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='suggested_dishes/')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Suggested Dish'
        verbose_name_plural = 'Suggested Dishes'

    def __str__(self):
        return self.name
    
class UserReview(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} - Rating: {self.rating}"