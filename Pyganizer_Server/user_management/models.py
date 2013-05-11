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
        return self.userAuth.name
    
    class Meta:
        ordering = ('')


