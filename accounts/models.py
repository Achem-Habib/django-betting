from operator import truediv

import channels.layers
from asgiref.sync import async_to_sync
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    club_name = models.CharField(max_length=100, blank=True, null=True)
    balance = models.FloatField(default=0)
    club_holder = models.BooleanField(default=False)
    total_bet = models.FloatField(default=0, null=True, blank=True)
    last_bet_date = models.DateTimeField(null=True, blank=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        channel_layer = channels.layers.get_channel_layer()
        group = f"job-posting"
        async_to_sync(channel_layer.group_send)(
            group,
            {
                "type": "propagate_status",
                "message": {"Changed" : "UserData "},
            },
        )

    class Meta:
        ordering = ['-date_joined',]
        
    def __str__(self):
        return self.username



class ClubProfit(models.Model):
    profit = models.FloatField(default=0)




