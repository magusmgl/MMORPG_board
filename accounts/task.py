from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import OneTimeCode


@shared_task
def send_onetme_code_to_email(pk):
    obj = OneTimeCode.objects.get(pk=pk)
    code = obj.code
    user = obj.user
    email = obj.user.email
    email_html = create_email_template(user,
                                       code,
                                       template='accounts/email_send_onetime_code.html')
    send_email(html_content=email_html,
               letter_subject='Login Confirmation',
               email_to=email)


def create_email_template(user, code, template):
    html = render_to_string(
        template_name=template,
        context={
            'user': user,
            'code': code
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
