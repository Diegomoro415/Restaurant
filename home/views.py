from django.shortcuts import render, redirect, get_object_or_404
from .models import UserReview
from .forms import UserReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_view(request):
    """
    Display the home page with user reviews and a form to submit new reviews.

    :param request: The HTTP request object.
    :return: Rendered HTML template for the home page.
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = UserReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.save()
                messages.success(request,
                                 'Your review has been sent successfully!')
                return redirect('home:home_view')
        else:
            messages.error(request, 'You need to login to write a review.')
            return redirect('login')
    else:
        form = UserReviewForm()

    user_reviews = UserReview.objects.all()

    context = {
        'user_reviews': user_reviews,
        'form': form,
    }

    return render(request, 'Home/home.html', context)


@login_required
def create_review(request):
    """
    Create a new review (requires user to be logged in).

    :param request: The HTTP request object.
    :return: Rendered HTML template for creating a review.
    """
    if request.method == 'POST':
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request,
                             'Your review has been created successfully!')
            return redirect('home:home_view')
    else:
        form = UserReviewForm()

    context = {
        'form': form,
    }
    return render(request, 'Home/home.html', context)


def user_reviews(request):
    """
    Display a page showing all user reviews.

    :param request: The HTTP request object.
    :return: Rendered HTML template for displaying user reviews.
    """
    reviews = UserReview.objects.all()
    return render(request, 'Home/user_reviews.html', {'user_reviews': reviews})


def edit_review(request, pk):
    """
    Edit an existing review.

    :param request: The HTTP request object.
    :param pk: The primary key of the review to be edited.
    :return: Rendered HTML template for editing a review.
    """
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        form = UserReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully!')
            return redirect('home:home_view')
    else:
        form = UserReviewForm(instance=review)
    return render(request, 'Home/edit_review.html', {'form': form})


def delete_review(request, pk):
    """
    Delete a review.

    :param request: The HTTP request object.
    :param pk: The primary key of the review to be deleted.
    :return: Rendered HTML template for deleting a review.
    """
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        messages.error(request, 'Your review has been deleted successfully!')
        return redirect('home:home_view')

    context = {
        'review': review,
    }

    return render(request, 'Home/home.html', context)
