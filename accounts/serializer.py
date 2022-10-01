from dataclasses import fields

from django.contrib.auth.password_validation import validate_password
from pyexpat import model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import ClubProfit, CustomUser, Message


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):   
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        token['email'] = user.email
        token['mobile_number'] = user.mobile_number
        token['club_name'] = user.club_name
        token['balance'] = user.balance
        token['club_holder'] = user.club_holder
        # ...
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'mobile_number', 'password', 'password2', 'club_name')

    def validate(self, attrs):
        email = CustomUser.objects.filter(email__iexact=attrs['email'])
        if email.exists():
            raise serializers.ValidationError({"error": "The email you entered is already exist.Try with  another email"})

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"error": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email = validated_data['email'],
            mobile_number = validated_data['mobile_number'],
            club_name = validated_data['club_name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



class UserBalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["balance", "is_active"]


class UpdatePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["password",]


class UpdateClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["club_name",]

class ClubNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username", "is_staff"]


class ClubMemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ["username", "date_joined", "total_bet", "last_bet_date"]


class TotalBetAndLastBetDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["total_bet", "last_bet_date",]



class ClubProfitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClubProfit
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = '__all__'
