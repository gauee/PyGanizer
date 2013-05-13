from django.db import models
from user_management.models import UserPyGanizer
import datetime
#from dateutil import parser

# Create your models here.

class MsgManager(models.Manager):
    
    def create_base_msg(self,user,msgHeader):
        baseMsg = Msg()
        baseMsg.createTime = datetime.datetime.now()
        baseMsg.userId = user
        baseMsg.msgHeader = msgHeader
        baseMsg.save()
        
        return baseMsg
    
    def create_event(self,user,msgHeader,start,end,category):
        baseMsg = self.create_base_msg(user,msgHeader)
        extendMsg = Event()
        extendMsg.msgId = baseMsg
        extendMsg.start = start
        extendMsg.end = end
        extendMsg.category = category
        extendMsg.save()
        
        return extendMsg
    
    def create_msg_to_friend(self,fromUser,toUser,msgHeader,msgBody):
        baseMsg = self.create_base_msg(toUser,msgHeader)
        extendMsg = MsgFromFriend()
        extendMsg.msgId = baseMsg
        extendMsg.fromUser = fromUser
        extendMsg.msgBody = msgBody
        extendMsg.save()
        
        return extendMsg
    
    def create_sticky_note(self,user,msgHeader,endtime,category):
        baseMsg = self.create_base_msg(user,msgHeader)
        extendMsg = StickyNote()
        extendMsg.msgId = baseMsg
        extendMsg.endtime = endtime
        extendMsg.category = category
        extendMsg.save()
        
        return extendMsg
        
    def create_comment_note(self,user,msgHeader,mainText):
        baseMsg = self.create_base_msg(user,msgHeader)
        extendMsg = Comment()
        extendMsg.msgId = baseMsg
        extendMsg.mainText = mainText
        extendMsg.save()
        
        return extendMsg
    
    def get_all_messages(self,user):
        print(user)
        print(user.id)
        return MsgFromFriend.objects.filter(msgId__userId = user)

class Msg(models.Model):
    createTime = models.DateTimeField('date published')
    msgHeader = models.CharField(max_length=100)
    userId = models.ForeignKey(UserPyGanizer)
    
class MsgFromFriend(models.Model):
    msgId = models.OneToOneField('Msg')
    fromUser = models.ForeignKey(UserPyGanizer)
    msgBody = models.CharField(max_length=1000)
    isRead = models.BooleanField(default=False)
    objects = MsgManager()
    
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
