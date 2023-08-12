from django.urls import path
from . import views

app_name = 'contact_us'

urlpatterns = [
    path('', views.contact_us_view, name='contact_us'),
    path('404/', views.handler404, name='handler404'),
    path('403/', views.handler403, name='handler403'),
    path('500/', views.handler500, name='handler500'),
]