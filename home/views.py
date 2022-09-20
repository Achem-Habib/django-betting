from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from home import serializer
from home.models import BetQuestion, BetRate, Match, MatchCategory
from home.serializer import (BetQuestionSerializer, BetRateSerializer,
                             MatchCategorySerializer, MatchSerializer,
                             SingleBetRateSerializer, SingleQuestionSerializer)


class MatchCategoryView(APIView):
    def get(self, request, format=None):
        category_id = self.request.query_params.get('id')
        category = MatchCategory.objects.get(id=category_id)
        serializer = MatchCategorySerializer(category)
        return Response(serializer.data)

class MatchList(APIView):
  
    #List all snippets, or create a new snippet.

    def get(self, request, format=None):
        matches = Match.objects.filter(show=True)
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionList(APIView):
  
    #List all snippets, or create a new snippet.

    def get(self, request, format=None):
        match_id = self.request.query_params.get('id')
        questions = BetQuestion.objects.filter(match=match_id, show=True)
        serializer = BetQuestionSerializer(questions, many=True)
        return Response(serializer.data)


class SingleQuestion(APIView):

    def get(self, request, format=None):
        question_id = self.request.query_params.get('id')
        question = BetQuestion.objects.get(id=question_id)
        serializer = SingleQuestionSerializer(question)
        return Response(serializer.data)


class BetRateList(APIView):
  
    #List all snippets, or create a new snippet.

    def get(self, request, format=None):
        question_id = self.request.query_params.get('id')
        bet_rates = BetRate.objects.filter(bet_question=question_id)
        serializer = BetRateSerializer(bet_rates, many=True)
        return Response(serializer.data)


class SingleBetRate(APIView):

    def get(self, request, format=None):
        bet_id = self.request.query_params.get('id')
        bet_rate = BetRate.objects.get(id=bet_id)
        serializer = SingleBetRateSerializer(bet_rate)
        return Response(serializer.data)
