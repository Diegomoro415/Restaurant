from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
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
            return redirect('home:home')  # Send user to home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'Accounts/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')  # Redirect user to home page after register
    else:
        form = UserCreationForm()  # Move this line outside of the if block

    return render(request, 'Accounts/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been successfully logged out.', extra_tags='error')
    return redirect('home:home')  # Redirect user to login page after logout
