from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    time = models.TimeField(auto_now=True)
    replyFrom = models.ForeignKey(self, blank=True)
    
class Post(models.Model):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    time = models.TimeField(auto_now=True)
    