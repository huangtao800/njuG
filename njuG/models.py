# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils import timezone
from django.conf import settings
from sorl.thumbnail import ImageField
from datetime import datetime 

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
    time = models.DateTimeField(auto_now=False, default=timezone.now)
    
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
    def __unicode__(self): 
        return u'%s' % self.content

class Comment(Event):
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    replyTo = models.ForeignKey("self", null=True)   # a comment might reply another
    def __unicode__(self): 
        return u'%s' % self.content
    
    
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
    viewCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
    def __unicode__(self): 
        return u'%s' % self.title
    
class BlogComment(Event):
    content = models.TextField()
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    replyTo = models.ForeignKey("self", null=True, blank=True)  ## reply someone's comment
    masterComment = models.ForeignKey("self", null=True, blank=True, related_name="first_blog_comment")    ## the first comment of a group of related blogComments
    def __unicode__(self): 
        return u'%s' % self.content
    
class Profile(models.Model):
    user = models.OneToOneField(User)
    nickName = models.CharField(max_length=30, default="无昵称")
    school = models.CharField(max_length=10, choices=settings.SCHOOL_LIST, default=u'南京大学')
    
    BIRTH_YEAR_CHOICES = [(i,i) for i in range(1970,2005)]
    birth_year = models.IntegerField(choices=BIRTH_YEAR_CHOICES, default=1995)
    
    TOP = u'攻'
    BOTTOM = u'受'
    VERS = u'不限'
    NOROLE = u'保密'
    ROLE_CHOICES = (
        (BOTTOM, u'受'),
        (TOP, u'攻'),
        (VERS, u'不限'),
        (NOROLE, '-'))
    role = models.CharField(max_length=5 ,choices = ROLE_CHOICES, default = NOROLE)
    
    UNDERGRAD = u'本科'
    GRAD = u'硕士'
    POSTGRAD = u'博士'
    DEGREE_CHOICES = (
        (UNDERGRAD, u'本科'),
        (GRAD, u'硕士'),
        (POSTGRAD, u'博士'))
    degree = models.CharField(max_length=3, choices = DEGREE_CHOICES, default = UNDERGRAD)
    hasAvatar = models.BooleanField(default=False)
    avatarType = models.CharField(max_length=6, default='jpg')
    unreadMessageCount = models.IntegerField(default=0)
    
    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year
    
    def __unicode__(self): 
        return u'%s' % self.nickName

class Message(models.Model):
    time = models.DateTimeField(auto_now=False)
    isRead = models.BooleanField(default=False)
    source = models.ForeignKey(User, related_name="source")
    target = models.ForeignKey(User, related_name="target")
    
    POST_COMMENT = 1
    REPLY_POST_COMMENT = 2
    BLOG_COMMENT = 3
    REPLY_BLOG_COMMENT = 4
    LIKE_POST = 5
    PRIVATE_MESSAGE = 6
    TYPE_CHOICES = (
        (POST_COMMENT, 1),
        (REPLY_POST_COMMENT, 2),
        (BLOG_COMMENT, 3),
        (REPLY_BLOG_COMMENT, 4),
        (LIKE_POST, 5),
        (PRIVATE_MESSAGE, 6)
        )
    type = models.IntegerField(choices = TYPE_CHOICES, default=POST_COMMENT)
    masterPost = models.ForeignKey(Post, blank=True, null=True)
    postComment = models.ForeignKey(Comment, blank=True, null=True)
    
    masterBlog = models.ForeignKey(Blog, blank=True, null=True)
    blogComment = models.ForeignKey(BlogComment, blank=True, null=True)
    masterComment = models.ForeignKey(BlogComment, blank=True, null=True, related_name="master_comment")
    content = models.TextField()
    
    def __unicode__(self): 
        return u'%s' % self.content
    class Meta:
        ordering=['-time']


class Activity(models.Model):
    time = models.DateTimeField(auto_now=False, default=timezone.now)
    user = models.ForeignKey(User)
    interestCount = models.IntegerField(default=0)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    onlyForSchool = models.BooleanField(default=True)
    openToAll = models.BooleanField(default=False, blank=True)
    
    PRIVATE_MESSAGE = u'私信我'
    WECHAT = u'微信'
    CONTACT_LIST = ((PRIVATE_MESSAGE,u'私信我'),(WECHAT,u'微信'))
    contact = models.CharField(max_length=20, choices = CONTACT_LIST, default=PRIVATE_MESSAGE)
    detailContact = models.CharField(max_length=50, null=True, blank=True)
    openSchoolList = models.CharField(max_length=1000, null=True, blank=True)
    
    def __unicode__(self): 
        return u'%s' % self.title
    
    class Meta:
        ordering=['-time']
    