from rest_framework import serializers
from .models import Content, Rating
from django.contrib.auth.models import AnonymousUser

class ContentSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()
    num_ratings = serializers.IntegerField()
    user_rating = serializers.SerializerMethodField()

    def get_user_rating(self, obj):
        request = self.context.get('request')
        if request and not isinstance(request.user, AnonymousUser):
            user = request.user
            try:
                rating = Rating.objects.get(content=obj, user=user)
                return rating.rating
            except Rating.DoesNotExist:
                return None
        return None
    
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'average_rating', 'num_ratings', 'user_rating']
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['content_id', 'rating']

    def create_or_update_rating(self, user, content, rating):
        rating_instance, created = Rating.objects.update_or_create(
            user=user,
            content=content,
            defaults={'rating': rating}
        )
        return rating_instance

    def create(self, validated_data):
        user = self.context['request'].user
        content = validated_data['content']
        rating = validated_data['rating']
        return self.create_or_update_rating(user, content, rating)