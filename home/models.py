from datetime import date
from email.mime import image
from sre_constants import MAX_UNTIL
from time import time

import channels.layers
from asgiref.sync import async_to_sync
from django.db import models

# Create your models here.

class MatchCategory(models.Model):
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images')

    def __str__(self):
        return self.category


class Match(models.Model):
    MATCH_STATUS = (
    ("Live", "Live Match"),
    ("Upcoming", "Upcoming Match"),    
    )

    match_category = models.ForeignKey(MatchCategory, related_name='match_category', on_delete=models.CASCADE)
    match_status = models.CharField(
        max_length = 50,
        choices = MATCH_STATUS,
        default = 'Upcoming'
        )
    tournament_name = models.CharField(max_length=100, null=True, blank=True)
    team_1 = models.CharField(max_length=100)
    team_2 =  models. CharField(max_length=100)
    date_time = models.DateTimeField(null=True, blank=True)   
    score = models.CharField(max_length=400,blank=True)
    show = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = channels.layers.get_channel_layer()
        group = f"job-posting"
        async_to_sync(channel_layer.group_send)(
            group,
            {
                "type": "propagate_status",
                "message": {"Changed": "Match", },
            },
        )

    def __str__(self):
        return self.team_1 + " vs " + self.team_2


class BetQuestion(models.Model):
    match = models.ForeignKey(Match, related_name="bet_questions", on_delete=models.CASCADE)
    identifier = models.IntegerField(default=1, null=True, blank=True)
    question = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    show = models.BooleanField(default=True)
    STATUS = (
    ("pending", "Pending"),
    ("finish", "Finish"),
    ("cancel", "Cancel"),
    ("return", "Return"),   
    )

    status = models.CharField(
        max_length = 50,
        choices = STATUS,
        default = 'pending'
        )

    finished_date_time = models.DateTimeField(null=True, blank=True)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = channels.layers.get_channel_layer()
        group = f"job-posting"
        async_to_sync(channel_layer.group_send)(
            group,
            {
                "type": "propagate_status",
                "message": {"Changed": "BetQuestion", },
            },
        )

    def __str__(self):
        return self.question

class BetRate(models.Model):
    bet_question = models.ForeignKey(BetQuestion,related_name="bet_rates", on_delete=models.CASCADE)
    bet_answer = models.CharField(max_length=250)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    win = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = channels.layers.get_channel_layer()
        group = f"job-posting"
        async_to_sync(channel_layer.group_send)(
            group,
            {
                "type": "propagate_status",
                "message": {"Changed": "BetRate", },
            },
        )

    
    @property
    def match_name(self):
        return "%s"%(self.bet_question.match)


    def __str__(self):
        return self.bet_answer
