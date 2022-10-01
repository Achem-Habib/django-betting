from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import ClubProfit, CustomUser, Message


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ['-date_joined',]
    list_display = ["username","mobile_number", "club_name",  "balance", "is_active", 'club_holder',
     'date_joined', 'total_bet', 'last_bet_date',]
    fieldsets = (
        (('User'), {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'mobile_number', "club_name", 'balance')}),
        (('Permissions'), {'fields': ('club_holder', 'is_active','is_staff', 'is_superuser')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_editable = ("balance", "is_active", 'club_holder')
    list_filter = ("is_active", "club_holder")
    

@admin.register(ClubProfit)
class ClubProfitAdmin(admin.ModelAdmin):
    list_display = ("profit",)

@admin.register(Message)
class ClubProfitAdmin(admin.ModelAdmin):
    list_display = ("id", "message",)
    list_editable = ("message",)



