from django.core.management.base import BaseCommand
import json
from contentService.models import Content, Rating

class Command(BaseCommand):
    help = 'Load data from JSON file and update models'

    def handle(self, *args, **kwargs):
        json_file_path = 'ratings.json'

        with open(json_file_path, 'r') as f:
            data = json.load(f)

        for item in data:
            content_id = item['fields']['content_id']
            rating_value = item['fields']['rating']
            user_id = item['fields']['user_id']
            
            Rating.objects.create(content_id=content_id, user_id=user_id, rating=rating_value)
            
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
