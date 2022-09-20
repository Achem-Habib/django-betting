from django.contrib import admin

from .models import BetQuestion, BetRate, Match, MatchCategory

# Register your models here.

@admin.register(MatchCategory)
class MatchCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    list_editable = ('category',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("match_category", "match_status", "team_1", "team_2", "date_time", "score", "show")
    
    list_editable = ("match_status", "score", "show")



class BetRateInline(admin.StackedInline):
    model = BetRate
    


@admin.register(BetQuestion)
class BetQuestionAdmin(admin.ModelAdmin):
    list_display = ("match", "question", "active", "show", "status" )
    list_filter = ("match",)
    list_editable = ("question", "active", "show", "status")
    inlines = [BetRateInline]

    
@admin.register(BetRate)
class BetRateAdmin(admin.ModelAdmin):
    list_display = ("id", "match_name", "bet_question", "bet_answer", "rate", "win")
    list_editable = ("bet_question", "bet_answer", "rate", "win")
    list_filter = ("bet_question__match", "bet_question",)
    