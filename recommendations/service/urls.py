from service.views import feedDB, searchRecommendations
from django.urls import path
urlpatterns = [path('feed/', feedDB), path('recommend/', searchRecommendations)]