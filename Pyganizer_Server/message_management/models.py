from django.db import models

# Create your models here.

class Msg(models.Model):
    createTime = models.DateTimeField('date published')
    msgHeader = models.CharField(max_length=100)
    userId = models.ForeignKey('UserPyGanizer')