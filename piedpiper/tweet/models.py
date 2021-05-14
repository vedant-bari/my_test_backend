from django.db import models

from piedpiper.users.models import User
# Create your models here.

class UserFollowers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User,related_name="user_followers")

    def __str__(self):
        return self.user.email

class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=140)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


        
