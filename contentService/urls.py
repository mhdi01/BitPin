from django.urls import path
from .views import ContentListAPIView, RatingCreateAPIView

urlpatterns = [
    path('contents/list/', ContentListAPIView.as_view(), name='content-list'),
    path('ratings/', RatingCreateAPIView.as_view(), name='create_rating'),
]