from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


@shared_task
def send_email(username, to_email):
    htmly = get_template('email.html')
    data = { 'username': username}
    subject, from_email, to = 'welcome', 'ameotechnishant@gmail.com', to_email
    html_content = htmly.render(data)
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
