from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('balance/', views.UserBalanceView.as_view(), name='balance'),
    path('club-name/', views.ClubNameView.as_view(), name='club_name'),
    path('update-password/', views.UpdatePasswordView.as_view(), name='update_password'),
    path('update-club/', views.UpdateClubView.as_view(), name='update_club'),
    path('club-member/', views.ClubMemberView.as_view(), name='club_member'),
    path('total-bet/', views.TotalBetAndLastBetDateView.as_view(), name='update_total_bet'),
    path('club-profit/', views.ClubProfitView.as_view(), name='club_profit'),
    path('message/', views.MessageView.as_view(), name='message'),
    path('', views.getRoutes)
]

