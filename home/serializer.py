from dataclasses import fields

from pyexpat import model
from rest_framework import serializers

from .models import BetQuestion, BetRate, Match, MatchCategory


class MatchCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchCategory
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'


class BetQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetQuestion
        fields = '__all__'

class SingleQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetQuestion
        fields = '__all__'


class BetRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetRate
        fields = '__all__'    


class SingleBetRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetRate
        fields = '__all__'
