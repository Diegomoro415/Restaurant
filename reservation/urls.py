from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('', views.reservation_view, name='reservation'),
    path('reservation_options/', views.reservation_options_view, name='reservation_options'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    path('detail/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
]