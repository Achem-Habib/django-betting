from django.urls import path

from home import views

urlpatterns = [
    path('match-category/', views.MatchCategoryView.as_view()),
    path('matches/', views.MatchList.as_view()),
    path('questions/', views.QuestionList.as_view()),
    path('betrates/', views.BetRateList.as_view()),
    path('question/', views.SingleQuestion.as_view()),
    path('betrate/', views.SingleBetRate.as_view()),
    #path('matches/<int:pk>/', views.match_detail),
    
]
