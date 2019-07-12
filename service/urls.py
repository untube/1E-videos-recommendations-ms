from service.views import feedDbUser, feedDbVideo, searchRecommendations, purgeDbUser, purgeDbVideo
from django.urls import path
urlpatterns = [
    #recommendations/1/2/feedUSer
    path('feedUser', feedDbUser), 
    #path('<int:user_id>/ <int:category_id>/feedUser', feedDbUser), 
    #recommendations/1/2/5/feedVideo
    #recommendations/2/3/6/feedVideo
    #recommendations/3/3/4/feedVideo
    path('feedVideo', feedDbVideo),
    path('purgeVideo', purgeDbVideo), 
    path('purgeUser', purgeDbUser),
    #recommendations/0/recommend
    path('<int:user_id>/recommend', searchRecommendations)]