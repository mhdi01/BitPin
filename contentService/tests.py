from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Content, Rating

class RatingAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.content = Content.objects.create(title='Test Content', description='This is a test content')

    def test_create_rating(self):
        url = reverse('create_rating')
        data = {'content_id': self.content.id, 'rating': 4.5}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Rating.objects.count(), 1)

    def test_update_rating(self):
        rating = Rating.objects.create(content=self.content, user=self.user, rating=4.0)
        url = reverse('create_rating')
        data = {'content_id': self.content.id, 'rating': 3.5}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        rating.refresh_from_db()
        self.assertEqual(rating.rating, 3.5)
