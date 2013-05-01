from django.db import models
from django.contrib.auth.models import User

class UserPyGanizer(models.Model):
    userId = models.OneToOneField(User, related_name='profile')
    pyganizerPermites = models.CharField(max_length=20)
    
    def __str__(self):
        return "%s's profile" % self.userId
    
    #calledarId = models.ForeignKey(Pyganizer_calendar.Calendar)
    #toDoBoardId = models.ForeignKey(Pyganizer_board.Board)

#class Friends(models.Model):
#    userId = models.ForeignKey('User')
#    friendId = models.ForeignKey('User')


    
