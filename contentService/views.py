from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Content, Rating
from .serializers import ContentSerializer, RatingSerializer

class ContentListAPIView(generics.ListAPIView):
    serializer_class = ContentSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        queryset = Content.objects.prefetch_related('ratings').all()
        return queryset
    

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        content_id = self.request.data.get('content_id')
        rating = self.request.data.get('rating')

        if content_id is None or rating is None:
            raise serializers.ValidationError("Content ID and rating are required fields.")

        content = get_object_or_404(Content, id=content_id)
        serializer.create_or_update_rating(user, content, rating)