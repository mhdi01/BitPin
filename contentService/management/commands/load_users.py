from django.core.management.base import BaseCommand
import json
from contentService.models import User

class Command(BaseCommand):
    help = 'Load data from JSON file and update models'

    def handle(self, *args, **kwargs):
        json_file_path = 'users.json'

        with open(json_file_path, 'r') as f:
            data = json.load(f)

        for item in data:
            username = item['fields']['username']
            password = item['fields']['password']
            
            User.objects.create(username=username, password=password)
            
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
