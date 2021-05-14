from django.db import models
from rest_framework import serializers
from .models import UserFollowers, Tweet

class UserFollowersSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFollowers
        fields = ('__all__')


class TweetSerializers(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source ="user.full_name",required=False)
    class Meta:
        model = Tweet
        fields = ('__all__')
        read_only_fields = ('user_full_name',)
        