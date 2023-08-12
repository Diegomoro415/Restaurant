from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home_view'),
    path('user_reviews/', views.user_reviews, name='user_reviews'),
    path('create_review/', views.create_review, name='create_review'),
    path('edit_review/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:pk>/', views.delete_review, name='delete_review'),
]
