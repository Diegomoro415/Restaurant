from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirecionar para a página de boas-vindas após o login
    else:
        form = AuthenticationForm()

    return render(request, 'Accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirecionar para a página de boas-vindas após o registro
    else:
        form = UserCreationForm()

    return render(request, 'Accounts/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecionar para a página de login após o logout
