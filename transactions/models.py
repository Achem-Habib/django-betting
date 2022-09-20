from time import time

from accounts.models import CustomUser
from django.db import models


class Deposit_Method(models.Model):
    method_name = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.method_name


class Deposit_Number(models.Model):
    method = models.ForeignKey(Deposit_Method, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.number
    

class Deposit_Request(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    method = models.CharField(max_length=50, null=False)
    send_to = models.CharField(max_length=20, null=False)
    send_from = models.CharField(max_length=20, null=False)
    amount = models.FloatField()
    transaction_number = models.CharField(max_length=30, null=False)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    STATUS = (
    ("Pending", "Pending"),
    ("Confirmed", "Confirm"),
    ("Cancelled", "Cancel"),
    ("Returned", "Return"),   
    )

    status = models.CharField(
        max_length = 50,
        choices = STATUS,
        default = 'pending'
        )

    class Meta:
        ordering = ["-date_time"]

    def __str__(self):
        return self.method

class Deposit_Limit(models.Model):
    lowest_limit = models.FloatField()
    highest_limit = models.FloatField()



class Withdraw_Method(models.Model):
    method_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.method_name


class Withdraw_Account_Type(models.Model):
    method = models.ForeignKey(Withdraw_Method, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.account_type



class Withdraw_Request(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    method = models.CharField(max_length=30, null=False)
    account_type = models.CharField(max_length=30, null=False)
    send_to = models.CharField(max_length=20, null=False)
    amount =  models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    STATUS = (
    ("Pending", "Pending"),
    ("Confirmed", "Confirm"),
    ("Cancelled", "Cancel"), 
    )

    status = models.CharField(
        max_length = 50,
        choices = STATUS,
        default = 'pending'
        )

    class Meta:
        ordering = ["-date_time"]

    def __str__(self):
        return self.method

class Withdraw_Limit(models.Model):
    lowest_limit = models.FloatField(null=True, blank=True)
    highest_limit = models.FloatField(null=True, blank=True)
    club_lowest_limit = models.FloatField(null=True, blank=True)
    club_highest_limit = models.FloatField(null=True, blank=True)
