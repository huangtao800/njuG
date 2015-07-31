from njuG.models import Post, Like, Comment, Blog, BlogComment, Image, Profile, Message
from django.utils import timezone

def createMessage(source, target, **kwargs):
    type = kwargs['type']
    if(type==Message.POST_COMMENT or type==Message.REPLY_POST_COMMENT):
        content = kwargs['content']
        post = kwargs['post']
        message = Message(source=source, target=target, masterPost=post, content=content, time=timezone.now())
    elif(type==Message.BLOG_COMMENT or type==Message.REPLY_BLOG_COMMENT):
        content = kwargs['content']
        blog = kwargs['blog']
        message = Message(source=source, target=target, masterBlog=blog, content=content, time=timezone.now())
    target.profile.unreadMessageCount += 1
    target.profile.save()
    message.save()


def clearUnreadMessage(user):
    user.unreadMessageCount = 0
    messages = Message.objects.filter(target=user, isRead=False)
    for m in messages:
        m.isRead = True
        m.save()