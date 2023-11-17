from django.urls import path
from api import views

urlpatterns = [
    path('crossreading/create/', views.CrossReadingCreate.as_view()),
    path('crossreading/<int:pk>/', views.CrossReadingById.as_view()),
]
