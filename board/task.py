from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import Reply


@shared_task
def notification_about_receiving_new_reply(reply_pk):
    reply = Reply.objects.get(pk=reply_pk)
    username = reply.advertise.author.get_username()
    author_email = reply.advertise.author.email
    email_html = create_email_template(username, reply)
    send_email(html_content=email_html,
               letter_subject='New response to your ad',
               email_to=author_email)

def create_email_template(user, reply):
    html = render_to_string(
        template_name='board/email_for_adding_new_reply.html',
        context={
            'user': user,
            'reply': reply
        }
    )
    return html

def send_email(html_content, letter_subject, email_to):
    from_email = settings.DEFAULT_FROM_EMAIL
    msg = EmailMultiAlternatives(
        subject=letter_subject,
        from_email=from_email,
        to=[email_to],
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
