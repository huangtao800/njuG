from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    time = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(Event):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    likes = models.BigIntegerField(default=0)
    
    def comments(self):
        return self.comment_set.all().order_by("-time")

class Comment(Event):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    replyFrom = models.ForeignKey("self", null=True)   # a comment might reply another
    
class Like(Event):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
    class Meta:
        unique_together = ('user', 'post',) # one user cannot like a post repeatedly
    