from django.urls import path

from transactions import views

urlpatterns = [
    path('deposit-method/', views.DepositMethodView.as_view()),
    path('deposit-number/', views.DepositNumberView.as_view()),
    path('deposit-request/', views.DepositRequestView.as_view()),
    path('deposit-limit/', views.DepositLimitView.as_view()),

    path('withdraw-method/', views.WithdrawMethodView.as_view()),
    path('withdraw-account-type/', views.WithdrawAccountView.as_view()),
    path('withdraw-request/', views.WithdrawRequestView.as_view()),
    path('withdraw-limit/', views.WithdrawLimitView.as_view()),

    
]
