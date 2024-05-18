from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.cache import cache

from .tasks import update_content_rating_stats

class Content(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    average_rating = models.FloatField(default=0)
    num_ratings = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.set(f'content_average_rating_{self.id}', self.average_rating)
        cache.set(f'content_num_ratings_{self.id}', self.num_ratings)

    def __str__(self) -> str:
        return self.title

class Rating(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='ratings', db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_suspicious = models.BooleanField(default=False)

    class Meta:
        unique_together = ('content', 'user')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        update_content_rating_stats.delay(self.content_id)

    def __str__(self) -> str:
        return f"{self.content.title}_{self.user.username}"