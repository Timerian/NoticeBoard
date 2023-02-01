from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reply


# signal what checking Reply.
# If Reply was saved firstly and have False accept status, then author of article receive notice email.
# If Reply was changed (get True accept status), then author of Reply receive email about accept.
@receiver(post_save, sender=Reply)
def changeResponseStatus(sender, instance, created, **kwargs):
    if not instance.accepted and created:
        email = instance.article.author.email
        print(email)
        send_mail(
            subject="Response",
            message=f"You received a response from {instance.author.username} to your ad ({instance.article}).",
            from_email=None,
            recipient_list=[email, ],
            fail_silently=False
        )
    else:
        email = instance.author.email
        send_mail(
            subject="Your response has been accepted",
            message=f"Your response ({instance.text[:20]}) dated {instance.create_date} to the ad ({instance.article}) has been accepted.",
            from_email=None,
            recipient_list=[email, ],
            fail_silently=False
        )
