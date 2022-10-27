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
    email_html = create_email_template(username,
                                       reply,
                                       template='board/email_for_adding_new_reply.html')
    send_email(html_content=email_html,
               letter_subject='New response to your ad',
               email_to=author_email)


@shared_task
def notification_about_accept_reply(reply_pk):
    reply = Reply.objects.get(pk=reply_pk)
    username = reply.author.get_username()
    author_email = reply.author.email
    email_html = create_email_template(username,
                                       reply,
                                       template='board/email_for_accept_reply.html')
    send_email(html_content=email_html,
               letter_subject='Reply has been accepted',
               email_to=author_email)


def create_email_template(user, reply, template):
    html = render_to_string(
        template_name=template,
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
