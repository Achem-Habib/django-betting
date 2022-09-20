from django.contrib import admin

from .models import PlaceBet

# Register your models here.

@admin.register(PlaceBet)
class PlaceBetAdmin(admin.ModelAdmin):
    list_display = ("user",  "tournament_name", "team_1", "team_2",  "question",  "answer", "rate", "amount", "return_amount", "club_name", "date_time", "status" )
    list_filter = ("club_name", "date_time",)
    search_fields = ("user__username",)
    list_per_page = 20
    
    
