from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Like, Comment, Blog, BlogComment, Image, Profile, Message, Activity

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Profile)
