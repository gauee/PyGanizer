from django.db import models
from user_management.models import UserPyGanizer
import datetime
#from dateutil import parser

# Create your models here.

class MsgManager(models.Manager):
    def create_event(self,user,msgHeader,start,end,category):
        baseMsg = Msg()
        baseMsg.createTime = datetime.datetime.now()
        baseMsg.msgHeader = msgHeader
        baseMsg.userId = user
        baseMsg.save()
        extendMsg = Event()
        extendMsg.msgId = baseMsg
        extendMsg.start = start
        extendMsg.end = end
        extendMsg.category = category
        extendMsg.save()
        
        return extendMsg

class Msg(models.Model):
    createTime = models.DateTimeField('date published')
    msgHeader = models.CharField(max_length=100)
    userId = models.ForeignKey(UserPyGanizer)
    
class StickyNote(models.Model):
    msgId = models.OneToOneField('Msg')
    endtime = models.DateTimeField('end_Time')
    category = models.IntegerField()
    objects = MsgManager()
    
class Event(models.Model):
    msgId = models.OneToOneField('Msg')
    start = models.DateTimeField('date_starting_event')
    end = models.DateTimeField('date_ending_event')
    category = models.IntegerField()
    objects = MsgManager()
    
class Comment(models.Model):
    msgId = models.OneToOneField('Msg')
    mainText = models.CharField(max_length=1000)
    #TODO drzewko komentarzy
