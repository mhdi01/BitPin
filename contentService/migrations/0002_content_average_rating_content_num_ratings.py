# Generated by Django 4.2 on 2024-05-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
