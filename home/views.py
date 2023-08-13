from django.shortcuts import render, redirect, get_object_or_404
from .models import UserReview
from .forms import UserReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    # Handle form submission to create a new review
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

    # Retrieve all user reviews
    user_reviews = UserReview.objects.all()

    context = {
        'user_reviews': user_reviews,
        'form': form,
    }

    return render(request, 'Home/home.html', context)

@login_required
def create_review(request):
    # Handle form submission to create a new review (requires user to be logged in)
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Your review has been created successfully!')
            return redirect('home:home_view')
    else:
        form = UserReviewForm()
    
    context = {
        'form': form,
    }
    return render(request, 'Home/home.html', context)

def user_reviews(request):
    # Display a page showing all user reviews
    reviews = UserReview.objects.all()
    return render(request, 'Home/user_reviews.html', {'user_reviews': reviews})

def edit_review(request, pk):
    # Handle form submission to edit an existing review
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
    # Handle deletion of a review
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.error(request, 'Your review has been deleted successfully!')
        return redirect('home:home_view')
    
    context = {
        'review': review,
    }

    return render(request, 'Home/home.html', context)
