from django.shortcuts import render
from django.db.models import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import UserFollowers, Tweet
from .serializers import UserFollowersSerializers,TweetSerializers

from piedpiper.users.permissions import IsUserOrReadOnly
from piedpiper.users.models import User

class TweetListCreateView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializers
    permission_classes = (IsAuthenticated,)

    
    def get_queryset(self):
        if 'followers' in self.request.query_params:
            user_followers = UserFollowers.objects.filter(user=self.request.user).exists() 
            if user_followers:
                user_followers = UserFollowers.objects.get(user=self.request.user)
                queryset = self.queryset.filter(user__in=user_followers.followers.all()).order_by('-created_at')
            else:
                queryset = self.queryset.filter(user=self.request.user).order_by('-created_at')   
        else:    
            queryset = self.queryset.filter(user=self.request.user).order_by('-created_at')
        return queryset
        
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class UserFollowersListCreateView(generics.ListCreateAPIView):
    queryset =  UserFollowers.objects.all()
    serializer_class = UserFollowersSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.filter(user=self.request.user)
        return queryset


    def create(self, request, *args, **kwargs):
        print("user", request.user)
        user_followers = self.get_queryset()
        if user_followers:
            print("in followers")
            data = request.data.get('followers')
            print("request", data)
            
            updated_queryset = user_followers[0].followers.add(*data)
            serializer = self.get_serializer(updated_queryset) 
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


# class UserFollowersListCreateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset =  UserFollowers.objects.all()
#     serializer_class = UserFollowersSerializers
#     permission_classes = [IsUserOrReadOnly]
#     lookup_field = "user"


#     def get_queryset(self):
#         queryset = self.queryset
#         if isinstance(queryset, QuerySet):
#             # Ensure queryset is re-evaluated on each request.
#             queryset = queryset.filter(user=self.request.user)
#         return queryset


      