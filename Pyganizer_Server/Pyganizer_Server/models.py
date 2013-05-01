from django.db import models

class Msg(models.Model):
    createTime = models.DateTimeField('date published')
    msgHeader = models.CharField(max_length=100)
    
