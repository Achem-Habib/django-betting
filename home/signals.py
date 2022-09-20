import channels.layers
from accounts.models import ClubProfit, CustomUser
from asgiref.sync import async_to_sync
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from place_bet.models import PlaceBet

from home.models import BetQuestion, BetRate, Match

from .models import BetRate


@receiver(post_save, sender=BetQuestion, dispatch_uid="bet_resolve")
def bet_resolve(sender, instance, **kwargs):
    global profit
    club_profit = ClubProfit.objects.all()
    for i in club_profit:
        profit = i.profit

    if (instance.status == 'finish'):

        bet_rate = BetRate.objects.filter(bet_question = instance.id)
        won_answer_id = []
        lost_answer_id = []

        

        for rate in bet_rate:
            if (rate.win == True):
                won_answer_id.append(rate.id)
            else:
                lost_answer_id.append(rate.id)

        print(won_answer_id)
        print(lost_answer_id)

        bet_to_resolve = PlaceBet.objects.filter(match_id = instance.match.id, question_id=instance.id, 
            question_identifier=instance.identifier, status="pending")

        for bet in bet_to_resolve:
            if (bet.answer_id in won_answer_id):
                bet.status = 'won'
                bet.save()
                
                if (bet.club_name):
                    club_holder = CustomUser.objects.get(username = bet.club_name)
                    club_commission = bet.amount * profit
                    club_holder.balance += club_commission
                    club_holder.save()


                user_amount_return = bet.return_amount - (bet.amount * profit)
                bet.user.balance += user_amount_return
                bet.user.save()
            else:
                bet.status = 'lost'
                bet.save()

                if (bet.club_name):
                    club_holder = CustomUser.objects.get(username = bet.club_name)
                    club_commission = bet.amount * profit
                    club_holder.balance += club_commission
                    club_holder.save()


    if(instance.status == 'cancel'):


        bet_to_resolve = PlaceBet.objects.filter(match_id = instance.match.id, question_id=instance.id, 
            question_identifier=instance.identifier, status="pending")

        for bet in bet_to_resolve:
            bet.status = 'cancelled'
            bet.save()

            bet.user.balance += bet.amount
            bet.user.save()
    
    if(instance.status == 'return'):

        bet_to_resolve = PlaceBet.objects.filter(match_id = instance.match.id, question_id=instance.id, 
            question_identifier=instance.identifier)


        for bet in bet_to_resolve:
            if (bet.status == 'won'):
                bet.status = 'pending'
                bet.save()

                if (bet.club_name):
                    club_holder = CustomUser.objects.get(username = bet.club_name)
                    club_commission = bet.amount * profit
                    club_holder.balance -= club_commission
                    club_holder.save()

                user_amount_return = bet.return_amount - (bet.amount * profit)
                bet.user.balance -= user_amount_return
                bet.user.save()

            elif (bet.status == 'lost'):
                bet.status = 'pending'
                bet.save()

                if (bet.club_name):
                    club_holder = CustomUser.objects.get(username = bet.club_name)
                    club_commission = bet.amount * profit
                    club_holder.balance -= club_commission
                    club_holder.save()

 

@receiver(post_delete, sender=Match, dispatch_uid="update_match")
def update_match(sender, instance, **kwargs):
    channel_layer = channels.layers.get_channel_layer()
    group = f"job-posting"
    async_to_sync(channel_layer.group_send)(
        group,
        {
            "type": "propagate_status",
            "message": {"Changed": "Match", },
        },
    )

@receiver(post_delete, sender=BetQuestion, dispatch_uid="update_bet_question")
def update_bet_question(sender, instance, **kwargs):
    channel_layer = channels.layers.get_channel_layer()
    group = f"job-posting"
    async_to_sync(channel_layer.group_send)(
        group,
        {
            "type": "propagate_status",
            "message": {"Changed": "BetQuestion", },
        },
    )

@receiver(post_delete, sender=BetRate, dispatch_uid="update_bet_rate")
def update_bet_rate(sender, instance, **kwargs):
    channel_layer = channels.layers.get_channel_layer()
    group = f"job-posting"
    async_to_sync(channel_layer.group_send)(
        group,
        {
            "type": "propagate_status",
            "message": {"Changed": "BetRate", },
        },
    )
