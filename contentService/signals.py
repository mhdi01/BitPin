from django.db.models.signals import post_save
from django.dispatch import receiver

from .tasks import detect_suspicious_activity
from .models import Rating

@receiver(post_save, sender=Rating)
def handle_rating_submission(sender, instance, created, **kwargs):
    if created:
        detect_suspicious_activity.delay(instance.content_id)
