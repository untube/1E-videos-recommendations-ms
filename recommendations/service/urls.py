from service.views import feedDbUser, feedDbVideo, searchRecommendations
from django.urls import path
urlpatterns = [path('feedUser/', feedDbUser), path('feedVideo/', feedDbVideo), path('recommend/', searchRecommendations)]