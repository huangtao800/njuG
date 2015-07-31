# -*- coding: utf-8 -*-
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
    time = models.DateTimeField(auto_now=False)
    
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
    
class Profile(models.Model):
    user = models.OneToOneField(User)
    nickName = models.CharField(max_length=30, default="无昵称")
    NJU = 'NJU'
    OTHER = 'OTHER'
    SCHOOL_CHOICES = (
        (NJU, '南京大学'),
        (OTHER, '其他学校'))
    school = models.CharField(max_length=10, choices=SCHOOL_CHOICES, default=NJU)
    
    TOP = '攻'
    BOTTOM = '受'
    VERS = '不限'
    NOROLE = '保密'
    ROLE_CHOICES = (
        (BOTTOM, '受'),
        (TOP, '攻'),
        (VERS, '不限'),
        (NOROLE, '-'))
    role = models.CharField(max_length=5 ,choices = ROLE_CHOICES, default = NOROLE)
    
    UNDERGRAD = '本科'
    GRAD = '硕士'
    POSTGRAD = '博士'
    DEGREE_CHOICES = (
        (UNDERGRAD, '本科'),
        (GRAD, '硕士'),
        (POSTGRAD, '博士'))
    degree = models.CharField(max_length=3, choices = DEGREE_CHOICES, default = UNDERGRAD)
    hasAvatar = models.BooleanField(default=False)
    avatarType = models.CharField(max_length=6, default='jpg')
    unreadMessageCount = models.IntegerField(default=0)

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
    TYPE_CHOICES = (
        (POST_COMMENT, 1),
        (REPLY_POST_COMMENT, 2),
        (BLOG_COMMENT, 3),
        (REPLY_BLOG_COMMENT, 4),
        (LIKE_POST, 5)
        )
    type = models.IntegerField(choices = TYPE_CHOICES, default=POST_COMMENT)
    masterPost = models.ForeignKey(Post, blank=True, null=True)
    masterBlog = models.ForeignKey(Blog, blank=True, null=True)
    content = models.TextField()
    