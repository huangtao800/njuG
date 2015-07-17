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
        
        
class Picture(models.Model):
    """This is a small demo using just two fields. The slug field is really not
    necessary, but makes the code simpler. ImageField depends on PIL or
    pillow (where Pillow is easily installable in a virtualenv. If you have
    problems installing pillow, use a more generic FileField instead.

    """
    file = models.ImageField(upload_to="pictures")
    slug = models.SlugField(max_length=50, blank=True)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return reverse('uploadPicNew', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)
        
        
class Blog(Event):
    title = models.CharField(max_length=300)
    content = models.TextField()
    user = models.ForeignKey(User)
    isAnonymous = models.BooleanField(default=False)