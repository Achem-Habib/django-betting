from django.urls import path

from place_bet import views

urlpatterns = [
    path('club-history/', views.ClubHistoryView.as_view()),
    path('', views.PlaceBetView.as_view()),
    

    
]
