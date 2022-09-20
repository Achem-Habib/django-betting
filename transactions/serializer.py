from accounts.models import CustomUser
from rest_framework import serializers

from .models import (Deposit_Limit, Deposit_Method, Deposit_Number,
                     Deposit_Request, Withdraw_Account_Type, Withdraw_Limit,
                     Withdraw_Method, Withdraw_Request)


class DepositMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit_Method
        fields = ["id", "method_name",]

class DepositNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit_Number
        fields = ["id", "number" , "method"]

class DepositRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit_Request
        fields = "__all__"

class DepositLimitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit_Limit
        fields = "__all__"

    
    
class WithdrawMethodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdraw_Method
        fields = ["id", "method_name",]


class WithdrawAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdraw_Account_Type
        fields = ["id", "account_type", "method"]

class WithdrawRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdraw_Request
        fields = "__all__"

class WithdrawLimitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdraw_Limit
        fields = "__all__"
