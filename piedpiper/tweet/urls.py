from django.urls import path
from .views import UserFollowersListCreateView, TweetListCreateView 
# UserFollowersListCreateView


urlpatterns = [
    path('tweetlistcreate/', TweetListCreateView.as_view()),
    path('userfollowerlistcreate/', UserFollowersListCreateView.as_view()),
    # path('userfollowerretriveupdatedelete/', UserFollowersListCreateView.as_view()),

] 
