from django.http import JsonResponse
from django.shortcuts import render
from home import serializer
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializer import (ClubMemberSerializer, ClubNameSerializer,
                                 ClubProfitSerializer,
                                 MyTokenObtainPairSerializer,
                                 RegisterSerializer,
                                 TotalBetAndLastBetDateSerializer,
                                 UpdateClubSerializer,
                                 UpdatePasswordSerializer,
                                 UserBalanceSerializer)

from .models import ClubProfit, CustomUser

# Create your views here.



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/accounts/token/',
        '/accounts/register/',
        '/accounts/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)



class UserBalanceView(APIView):

    def get(self, request, format=None):
        user_name = self.request.query_params.get('user_name')
        user_balance = CustomUser.objects.get(username = user_name)
        serializer = UserBalanceSerializer(user_balance)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_name = self.request.query_params.get('user_name')
        item = CustomUser.objects.get(username = user_name)
        serializer = UserBalanceSerializer(instance=item, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePasswordView(APIView):
    def post(self, request, format=None):
        user_name = self.request.query_params.get('user_name')
        user = CustomUser.objects.get(username = user_name)
        serializer = UpdatePasswordSerializer(instance=user, data=request.data)
        
        if serializer.is_valid():
            user.set_password(request.data['password'])
            user.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateClubView(APIView):
    def post(self, request, format=None):
        user_name = self.request.query_params.get('user_name')
        item = CustomUser.objects.get(username = user_name)
        serializer = UpdateClubSerializer(instance=item, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClubNameView(APIView):
    
    def get(self, request, format=None):
        club_name = CustomUser.objects.filter(club_holder=True)
        serializer = ClubNameSerializer(club_name, many=True)
        return Response(serializer.data)


class ClubMemberView(APIView):

    def get(self, request, format=None):
        club_name = self.request.query_params.get('club_name')
        users = CustomUser.objects.filter(club_name = club_name)
        serializer = ClubMemberSerializer(users, many=True)

        return Response(serializer.data)


class TotalBetAndLastBetDateView(APIView):

    def get(self, request, format=None):
        user_name = self.request.query_params.get('user_name')
        user = CustomUser.objects.get(username = user_name)
        serializer = TotalBetAndLastBetDateSerializer(user)

        return Response(serializer.data)


    def post(self, request, format=None):
        user_name = self.request.query_params.get('user_name')
        item = CustomUser.objects.get(username = user_name)
        serializer = TotalBetAndLastBetDateSerializer(instance=item, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClubProfitView(APIView):

    def get(self, request, format=None):
        profit = ClubProfit.objects.all()
        serializer = ClubProfitSerializer(profit, many=True)
        
        return Response(serializer.data)
