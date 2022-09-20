from datetime import date

from accounts.models import CustomUser
from django.db import models

# Create your models here.


class PlaceBet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, )
    username = models.CharField(max_length=250, null=True, blank=True)
    match_id = models.IntegerField()
    match_category = models.CharField(max_length=100)
    tournament_name = models.CharField(max_length=200, null=True, blank=True)
    match_date_time = models.DateTimeField(null=True, blank=True)
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
 
    question_id = models.IntegerField()
    question_identifier = models.IntegerField(null=True, blank=True)
    question = models.CharField(max_length=250)

    answer_id = models.IntegerField()
    answer = models.CharField(max_length=250)
    rate = models.FloatField()

    club_name = models.CharField(max_length=250, null=True, blank=True)
    amount = models.FloatField(default=0)
    return_amount = models.FloatField(default=0)
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    STATUS = (
    ("pending", "Pending"),
    ("won", "Won"),
    ("lost", "Lost"),
    ("cancelled", "Cancelled")    
    )
    status = models.CharField(
        max_length = 50,
        choices = STATUS,
        default = 'pending'
        )

    class Meta:
        ordering = ["-date_time"]
        
    def __str__(self):
        return self.answer
