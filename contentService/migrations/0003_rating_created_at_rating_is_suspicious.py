# Generated by Django 4.2 on 2024-05-17 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contentService', '0002_content_average_rating_content_num_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='is_suspicious',
            field=models.BooleanField(default=False),
        ),
    ]
