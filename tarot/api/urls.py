from django.urls import path
from api import views

urlpatterns = [
    path('cards/', views.GetCards.as_view()),
    path('cards/<int:pk>/', views.GetCard.as_view()),
]