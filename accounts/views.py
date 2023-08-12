from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, 'You have been successfully logged in.', extra_tags='success')
            return redirect('reservation:reservation')  # Send user to reservation page after login
    else:
        form = AuthenticationForm()

    return render(request, 'Accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and log in the user
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('reservation:reservation')  # Redirect user to reservation page after register
            else:
                messages.error(request, 'Registration successful, but login failed. Please try logging in.')
                return redirect('accounts:login')  # Redirect user to login page
    else:
        form = UserCreationForm()

    return render(request, 'Accounts/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been successfully logged out.', extra_tags='error')
    return redirect('home:home')  # Redirect user to login page after logout
