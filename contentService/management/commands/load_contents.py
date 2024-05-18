from django.core.management.base import BaseCommand
import json
from contentService.models import Content, Rating

class Command(BaseCommand):
    help = 'Load data from JSON file and update models'

    def handle(self, *args, **kwargs):
        json_file_path = 'contents.json'

        with open(json_file_path, 'r') as f:
            data = json.load(f)

        for item in data:
            title = item['fields']['title']
            description = item['fields']['description']
            
            Content.objects.create(title=title, description=description)
            
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
