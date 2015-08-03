from njuG.models import Post, Like, Comment, Blog, BlogComment, Image, Profile, Message
from django.utils import timezone

def createMessage(source, target, **kwargs):
    type = kwargs['type']
    if(type==Message.POST_COMMENT or type==Message.REPLY_POST_COMMENT):
        content = kwargs['content']
        post = kwargs['post']
        postComment = kwargs['postComment']
        message = Message(source=source, target=target, type=type, 
                masterPost=post, content=content, postComment=postComment, time=timezone.now())
    elif(type==Message.BLOG_COMMENT or type==Message.REPLY_BLOG_COMMENT):
        content = kwargs['content']
        blog = kwargs['blog']
        blogComment = kwargs['blogComment']
        if type==Message.REPLY_BLOG_COMMENT:
            masterComment = kwargs['masterComment']
            message = Message(source=source, target=target, type=type, 
                    masterBlog=blog, content=content, blogComment=blogComment, masterComment=masterComment, time=timezone.now())
        else:
            message = Message(source=source, target=target, type=type, 
                    masterBlog=blog, content=content, blogComment=blogComment, time=timezone.now())
    elif(type==Message.PRIVATE_MESSAGE):
        content = kwargs['content']
        message = Message(source=source, target=target, type=type, content=content, time=timezone.now())
    target.profile.unreadMessageCount += 1
    target.profile.save()
    message.save()


def clearUnreadMessage(user):
    user.unreadMessageCount = 0
    messages = Message.objects.filter(target=user, isRead=False)
    for m in messages:
        m.isRead = True
        m.save()