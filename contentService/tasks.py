# contentService/tasks.py
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count, Avg

TIME_WINDOW = timezone.timedelta(hours=1)
RATING_COUNT_THRESHOLD = 100
LOW_RATING_THRESHOLD = 2.0
HIGH_RATING_THRESHOLD = 4.0
SUSPICIOUS_RATING_PERCENTAGE = 0.5
RATING_DIFFERENCE_THRESHOLD = 1.5


@shared_task()
def update_content_rating_stats(content_id):
    from .models import Content, Rating
    content = Content.objects.get(id=content_id)
    valid_ratings = Rating.objects.filter(content=content, is_suspicious=False)
    content.average_rating = valid_ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    content.num_ratings = valid_ratings.count()
    content.save()

@shared_task()
def detect_suspicious_activity(content_id):
    from .models import Content, Rating
    now = timezone.now()
    start_time = now - TIME_WINDOW

    content = Content.objects.get(id=content_id)
    recent_ratings = Rating.objects.filter(content_id=content_id, created_at__gte=start_time)

    num_recent_ratings = recent_ratings.count()

    low_ratings_count = recent_ratings.filter(rating__lte=LOW_RATING_THRESHOLD).count()
    high_ratings_count = recent_ratings.filter(rating__gte=HIGH_RATING_THRESHOLD).count()
    low_ratings_percentage = low_ratings_count / num_recent_ratings if num_recent_ratings else 0
    high_ratings_percentage = high_ratings_count / num_recent_ratings if num_recent_ratings else 0

    if num_recent_ratings > RATING_COUNT_THRESHOLD:
        if low_ratings_percentage > SUSPICIOUS_RATING_PERCENTAGE and content.average_rating - LOW_RATING_THRESHOLD > RATING_DIFFERENCE_THRESHOLD:
            for rating in recent_ratings.filter(rating__lte=LOW_RATING_THRESHOLD):
                rating.is_suspicious = True
                rating.save()

        if high_ratings_percentage > SUSPICIOUS_RATING_PERCENTAGE and HIGH_RATING_THRESHOLD - content.average_rating > RATING_DIFFERENCE_THRESHOLD:
            for rating in recent_ratings.filter(rating__gte=HIGH_RATING_THRESHOLD):
                rating.is_suspicious = True
                rating.save()

        update_content_rating_stats.delay(content_id)