from django.contrib import admin
from .models import Content, Rating

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'average_rating', 'num_ratings')
    search_fields = ('title',)
    readonly_fields = ('average_rating', 'num_ratings')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'rating', 'created_at', 'is_suspicious')
    list_filter = ('content',)
    search_fields = ('content__title', 'user__username')
