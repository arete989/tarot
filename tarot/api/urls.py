from django.urls import path
from api import views

urlpatterns = [
    path('cards/', views.get_all_cards),
    path('cards/<int:pk>/', views.get_one_card),
]