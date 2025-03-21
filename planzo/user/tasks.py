from celery import shared_task
from django.core.mail import send_mail
import uuid

@shared_task
def send_welcome_email(email):
    subject = "Welcome to Our Platform"
    message = f"Hi {email}, thank you for registering with us!"
    from_email = "no-reply@yourdomain.com"
    recipient_list = [email]
    print(message)
    return message


@shared_task
def make_verification_secreate(user):
    user.verication_secret = str(uuid.uuid4().hex)
    user.save()
    return user.verication_secret
