from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Deposit_Request


@receiver(post_save, sender=Deposit_Request, dispatch_uid="update_user_balance")
def update_user_balance(sender, instance, **kwargs):
    if (instance.status == "Confirmed"):
        instance.user.balance += instance.amount
        instance.user.save()
    if (instance.status == "Returned"):
        instance.user.balance -= instance.amount
        instance.user.save()
