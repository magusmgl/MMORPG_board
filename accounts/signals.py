from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OneTimeCode
from .task import (
    send_onetme_code_to_email,
    deleting_onetime_code
)


@receiver(post_save, sender=OneTimeCode)
def notify_users_for_email(sender, instance, created, **kwargs):
    if created:
        send_onetme_code_to_email.delay(pk=instance.pk)


@receiver(post_save, sender=OneTimeCode)
def deleting_onetime_code_after_five_minutes(sender, instance, created, **kwargs):
    if created:
        deleting_onetime_code.apply_async([instance.pk], countdown=300)
