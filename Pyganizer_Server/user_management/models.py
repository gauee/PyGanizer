from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User

class UserPyGanizerLabel(models.Model):
    label = models.CharField(max_length=40)
    orderId = models.IntegerField()

class UserPyGanizer(models.Model):
    userAuth = models.OneToOneField(User, related_name='profile')
    extraInfo = models.CharField(max_length=200)
    friends = models.ManyToManyField('UserPyGanizer')
    
    def __unicode__(self):
        return self.userAuth.username
    
    
class UserFasade(models.Manager):
    def get_user_friends(self,user):
        friends = list(user.profile.friends.all())
        print('friends ')
        print(friends)
        return friends
 
    def get_user_pyganizer_by_username(self,username):
        user = UserPyGanizer.objects.get(userAuth__username='gauee')
        return user
    
class UserFasadeInstance(models.Model):
    objects = UserFasade()
    

