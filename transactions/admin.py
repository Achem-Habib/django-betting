from django.contrib import admin

from .models import (Deposit_Limit, Deposit_Method, Deposit_Number,
                     Deposit_Request, Withdraw_Account_Type, Withdraw_Limit,
                     Withdraw_Method, Withdraw_Request)

# Register your models here.

class DepositNumberInline(admin.StackedInline):
    model = Deposit_Number
    

@admin.register(Deposit_Method)
class DepositMethodAdmin(admin.ModelAdmin):
    list_display = ("method_name", )
    inlines = [DepositNumberInline,]

@admin.register(Deposit_Number)
class DepositNumberAdmin(admin.ModelAdmin):
    list_display = ("method", "number")
    list_editable = ( "number",)

@admin.register(Deposit_Request)
class DepositRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "method", "send_to", "send_from", "amount", "transaction_number", "status", "date_time", )
    list_editable = ("amount", "status")
    list_filter = ("status", "send_to", "method", "date_time")
    search_fields = ("user__username", "send_from", "transaction_number")
    list_per_page = 20

@admin.register(Deposit_Limit)
class DepositLimitAdmin(admin.ModelAdmin):
    list_display = ("id", "lowest_limit", "highest_limit")
    list_editable = ("lowest_limit", "highest_limit")  
    


class WithdrawAccountInline(admin.StackedInline):
    model = Withdraw_Account_Type


@admin.register(Withdraw_Method)
class WithdrawMethodAdmin(admin.ModelAdmin):
    list_display = ("method_name", )
    inlines = [WithdrawAccountInline,]

@admin.register(Withdraw_Account_Type)
class WithdrawAccountAdmin(admin.ModelAdmin):
    list_display = ("method", "account_type")
    list_editable = ("account_type",)

@admin.register(Withdraw_Request)
class WithdrawRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "method", "account_type", "send_to", "amount", "date_time", "status")
    list_editable = ("status", "amount")
    list_filter = ("status", "send_to", "method", "date_time")
    search_fields = ("user__username", "transaction_number",)
    list_per_page = 20

@admin.register(Withdraw_Limit)
class withdrawLimitAdmin(admin.ModelAdmin):
    list_display = ("id", "lowest_limit", "highest_limit", "club_lowest_limit", "club_highest_limit")
    list_editable = ("lowest_limit", "highest_limit", "club_lowest_limit", "club_highest_limit")  
