from django.db.models.signals import post_save
from django.core.mail import mail_managers
from django.dispatch import receiver

from .models import Reply


@receiver(post_save, sender=Reply)
def notify_author_for_new_reply(sender, instance, created, **kwargs):
    mail_managers(
        subject=f'{instance.author} {instance.advertise}',
        message=instance.advertise
    )
