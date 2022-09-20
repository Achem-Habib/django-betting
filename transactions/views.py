from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions import serializer

from .models import (Deposit_Limit, Deposit_Method, Deposit_Number,
                     Deposit_Request, Withdraw_Account_Type, Withdraw_Limit,
                     Withdraw_Method, Withdraw_Request)
from .serializer import (DepositLimitSerializer, DepositMethodSerializer,
                         DepositNumberSerializer, DepositRequestSerializer,
                         WithdrawAccountSerializer, WithdrawLimitSerializer,
                         WithdrawMethodSerializer, WithdrawRequestSerializer)

# Create your views here.

class DepositMethodView(APIView):
    def get(self, request):
        depositMethod = Deposit_Method.objects.all()
        serializer = DepositMethodSerializer(depositMethod, many=True)
        return Response(serializer.data)

class DepositNumberView(APIView):
    def get(self, request):
        name = self.request.query_params.get('name')
        depositNumber = Deposit_Number.objects.filter(method__method_name = name)
        serializer = DepositNumberSerializer(depositNumber, many=True)
        return Response(serializer.data)

class DepositRequestView(APIView):

    def get(self, request, format=None):
        user_name = self.request.query_params.get('username')
        depositRequests = Deposit_Request.objects.filter(user__username = user_name)
        serializer = DepositRequestSerializer(depositRequests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepositRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepositLimitView(APIView):
    def get(self, request):
        deposit_limit = Deposit_Limit.objects.all()
        serializer = DepositLimitSerializer(deposit_limit, many=True)
        return Response(serializer.data)


class WithdrawMethodView(APIView):
    def get(self, request):
        withdrawMethod = Withdraw_Method.objects.all()
        serializer = WithdrawMethodSerializer(withdrawMethod, many=True)
        return Response(serializer.data)

class WithdrawAccountView(APIView):
    def get(self, request):
        account = self.request.query_params.get('account')
        withdrawAccount = Withdraw_Account_Type.objects.filter(method__method_name = account)
        serializer = WithdrawAccountSerializer(withdrawAccount, many=True)
        return Response(serializer.data)

class WithdrawRequestView(APIView):

    def get(self, request, format=None):
        user_name = self.request.query_params.get('username')
        withdrawRequests = Withdraw_Request.objects.filter(user__username = user_name)
        serializer = WithdrawRequestSerializer(withdrawRequests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WithdrawRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WithdrawLimitView(APIView):
    def get(self, request):
        withdraw_limit = Withdraw_Limit.objects.all()
        serializer = WithdrawLimitSerializer(withdraw_limit, many=True)
        return Response(serializer.data)
