from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PlaceBet
from .serializer import PlaceBetSerializer


class PlaceBetView(APIView):
  
    #List all snippets, or create a new snippet.

    def get(self, request, format=None):
        username = self.request.query_params.get('username')
        bet_list = PlaceBet.objects.filter(user__username=username)
        serializer = PlaceBetSerializer(bet_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceBetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClubHistoryView(APIView):

    def get(self, request, format=None):
        club_name = self.request.query_params.get('club_name')
        club_history = PlaceBet.objects.filter(club_name=club_name)
        serializer = PlaceBetSerializer(club_history, many=True)
        return Response(serializer.data)
