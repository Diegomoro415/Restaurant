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
                messages.success(request, 'Avaliação enviada com sucesso!')
                return redirect('home_view')  # Corrigir o nome da view para 'home_view'
        else:
            # Se o usuário não estiver autenticado, redireciona para a página de login ou exibe uma mensagem de erro
            messages.error(request, 'Você precisa fazer login para escrever uma avaliação.')
            return redirect('login')

    else:
        form = UserReviewForm()

    user_reviews = UserReview.objects.all()

    context = {
        'suggested_dishes': suggested_dishes,
        'user_reviews': user_reviews,
        'form': form,  # Passa o formulário para o contexto para que seja exibido na página
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
            return redirect('home:home_view')  # Redirecionar para a página inicial após a criação da avaliação
    else:
        form = UserReviewForm()

    return render(request, 'Home/create_review.html', {'form': form})

def user_reviews(request):
    reviews = UserReview.objects.all()
    return render(request, 'Home/user_reviews.html', {'user_reviews': reviews})

# View para editar uma avaliação
def edit_review(request, pk):
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        form = UserReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home:home_view')  # Redireciona para a página de avaliações após edição
    else:
        form = UserReviewForm(instance=review)
    return render(request, 'Home/edit_review.html', {'form': form})

# View para deletar uma avaliação
def delete_review(request, pk):
    review = get_object_or_404(UserReview, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('home:home_view')  # Redireciona para a página de avaliações após deleção
    return render(request, 'Home/delete_review.html', {'review': review})
