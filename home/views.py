from django.shortcuts import render, redirect, get_object_or_404
from .models import SuggestedDish, UserReview
from .forms import UserReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def home_view(request):
    suggested_dishes = SuggestedDish.objects.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = UserReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.save()
                messages.success(request, 'Your review has been sent successfully!')
                return redirect('home:home_view')
        else:
            messages.error(request, 'You need to login to write a review.')
            return redirect('login')

    else:
        form = UserReviewForm()

    user_reviews = UserReview.objects.all()

    context = {
        'suggested_dishes': suggested_dishes,
        'user_reviews': user_reviews,
        'form': form,
    }

    return render(request, 'Home/home.html', context)



def suggested_dishes(request):
    dishes = SuggestedDish.objects.all()

    context = {
        'dishes': dishes
    }
    return render(request, 'Home/suggested_dishes.html', context)


@login_required
def create_review(request):
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('home:home_view')
    else:
        form = UserReviewForm()

    return render(request, 'Home/create_review.html', {'form': form})

def user_reviews(request):
    reviews = UserReview.objects.all()
    return render(request, 'Home/user_reviews.html', {'user_reviews': reviews})

def edit_review(request, pk):
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        form = UserReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home:home_view')
    else:
        form = UserReviewForm(instance=review)
    return render(request, 'Home/edit_review.html', {'form': form})


def delete_review(request, pk):
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.error(request, 'Your review has been deleted successfully!')
        return redirect('home:home_view')
    
    return render(request, 'Home/delete_review.html', {'review': review})
