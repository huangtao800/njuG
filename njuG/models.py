from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    time = models.TimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(Event):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User)

class Comment(Event):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    replyFrom = models.ForeignKey("self", blank=True)   # a comment might reply another
    
    