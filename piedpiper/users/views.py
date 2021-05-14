from django.db.models import query
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializer
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib import messages
from django.http import HttpResponseRedirect

from piedpiper.tweet.models import Tweet, UserFollowers 

class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserListView(generics.ListAPIView):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)


    def get_queryset(self):
      followers_id=[]    
      print("user", self.request.user)
      user_followers = UserFollowers.objects.filter(user=self.request.user)
      if len(user_followers)>0:
          followers_id = [i.get('followers') for i in user_followers.values('followers')]
          
      followers_id.append(self.request.user.id)
      print("followers id", followers_id)
      queryset = self.queryset.exclude(id__in=followers_id)
      return queryset


