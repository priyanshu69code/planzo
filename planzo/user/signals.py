from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from user.tasks import send_welcome_email


@receiver(post_save, sender=User)
def user_created_signal(sender, instance, created, **kwargs):
    if created:
        # Trigger the Celery task to send an email
        send_welcome_email.delay(instance.email)

# She is said You are not capable of Love, Now Who will tell her that I Smile at strangers, Wave at babies and prey when I see an ambulance passes by.
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import make_verification_secreate


@receiver(post_save, sender=User)
def create_verification_secret(sender, instance, created, **kwargs):
    if created and not instance.verication_secret:
        make_verification_secreate.delay(instance.id)
