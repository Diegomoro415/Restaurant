from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# View to handle user login
def login_view(request):
    """
    Allows users to log in using the AuthenticationForm.
    Redirects to the reservation page upon successful login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(
                request,
                'You have been successfully logged in.',
                extra_tags='success')
            return redirect('reservation:reservation')
    else:
        form = AuthenticationForm()

    return render(request, 'Accounts/login.html', {'form': form})


# View to handle user registration
def register_view(request):
    """
    Allows users to register using the UserCreationForm.
    Authenticates and logs in the user upon successful registration.
    Redirects to the reservation page after successful registration and login.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and log in the user
            authenticated_user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(
                    request,
                    'Registration successful. You are now logged in.')
                return redirect(
                    'reservation:reservation'
                    )  # Redirect user to reservation page after register
            else:
                messages.error(
                    request,
                    "Registration successful, but login failed. "
                    "Please try logging in."
                    )
                return redirect(
                    'accounts:login'
                    )  # Redirect user to login page
    else:
        form = UserCreationForm()

    return render(request, 'Accounts/register.html', {'form': form})


# View to handle user logout (requires authentication)
@login_required
def logout_view(request):
    """
    Requires authentication. Logs the user out and redirects to the home page.
    """
    logout(request)
    messages.info(
        request,
        'You have been successfully logged out.',
        extra_tags='error'
        )
    return redirect('home:home')  # Redirect user to home page after logout
