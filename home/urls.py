from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('suggested_dishes/', views.suggested_dishes, name='suggested_dishes'),
    path('user_reviews/', views.user_reviews, name='user_reviews'),
]