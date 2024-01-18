from django.urls import path

from . import views

urlpatterns = [
    path('', views.FlashcardRequestHandler.as_view(), name='list-flashcards'),
    
    path('new-flashcard/', views.NewFlashcardRequestHandler.as_view(), name='new-flashcard'),
    path('del-flashcard/<int:pk>', views.DelFlashcardRequestHandler.as_view(), name='del-flashcard'),
    path('awnser-flashcard/<int:pk>', views.AwnserFlashcardRequestHandler, name='awnser-flashcard'),
    
    path('new-challenge/', views.NewChallengeRequestHandler.as_view(), name='new-challenge'),
    path('list-challenges/', views.ListChallengeRequestHandler.as_view(), name='list-challenges'),
    path('detail-challenge/<int:pk>', views.DetailChallengeRequestHandler.as_view(), name='detail-challenge'),

]