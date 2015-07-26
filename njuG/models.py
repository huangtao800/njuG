from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from sorl.thumbnail import ImageField

# Create your models here.
class Image(models.Model):
    file = ImageField(upload_to="images")
    user = models.ForeignKey(User)
 
@receiver(pre_delete, sender=Image)
def image_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if(instance.file):
        instance.file.delete(False)

class Event(models.Model):
    time = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ['-time']

class Post(Event):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User)
    likes = models.BigIntegerField(default=0)
    img1 = models.ForeignKey(Image, blank=True, null=True, related_name="img1")
    img2 = models.ForeignKey(Image, blank=True, null=True, related_name="img2")
    img3 = models.ForeignKey(Image, blank=True, null=True, related_name="img3")
    
    def comments(self):
        return self.comment_set.all().order_by("-time")

class Comment(Event):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    replyFrom = models.ForeignKey("self", null=True)   # a comment might reply another0
    
    
class Like(Event):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    
    class Meta:
        unique_together = ('user', 'post',) # one user cannot like a post repeatedly
        
        
        
class Blog(Event):
    title = models.CharField(max_length=300)
    content = models.TextField()
    user = models.ForeignKey(User)
    isAnonymous = models.BooleanField(default=False)
    
class BlogComment(Event):
    content = models.TextField()
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    replyTo = models.ForeignKey("self", null=True, blank=True)  ## reply someone's comment
    masterComment = models.ForeignKey("self", null=True, blank=True, related_name="first_blog_comment")    ## the first comment of a group of related blogComments