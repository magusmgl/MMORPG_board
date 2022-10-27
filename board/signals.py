from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Reply
from .task import notification_about_receiving_new_reply


@receiver(post_save, sender=Reply)
def notify_users_for_email(sender, instance, created, **kwargs):
    if created:
        notification_about_receiving_new_reply.delay(reply_pk=instance.pk)
    else:
        if instance.is_accept:
            pass
