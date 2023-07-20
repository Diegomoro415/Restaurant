from django.shortcuts import render
from .models import SuggestedDish, UserReview

# Create your views here.

def home_view(request):
    suggested_dishes = SuggestedDish.objects.all()
    user_reviews = UserReview.objects.all()
    
    context = {
        'suggested_dishes': suggested_dishes,
        'user_reviews': user_reviews,
    }
    
    return render(request, 'Home/home.html', context)


def suggested_dishes(request):
    dishes = SuggestedDish.objects.all()
    return render(request, 'Home/suggested_dishes.html', {'dishes': dishes})

def user_reviews(request):
    reviews = UserReview.objects.all()
    print(reviews)
    return render(request, 'Home/user_reviews.html', {'reviews': reviews})
