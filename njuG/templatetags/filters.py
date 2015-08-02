from django import template
from njuG.models import Post, Like, Comment, Blog, BlogComment, Image, Profile, Message

register = template.Library()

@register.filter(name = 'addCSS')
def addCSS(field, css):
    """Add CSS class to widget"""
    return field.as_widget(attrs={"class": css})

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)

@register.filter_function
def getAvatarPath(username):
    if(username):
        return "/static/img/avatar/" + username
    else:
        return "/static/img/avatar/Default-Avatar.jpg"
    
@register.filter_function
def getPosts(user):
    posts = Post.objects.filter(user = user)
    return posts

@register.filter_function
def isLikePost(user, post):
    like = Like.objects.filter(user=user,post=post).first()
    if(like):
        return True
    return False

@register.filter_function
def isPostComment(message):
    return message.type==Message.POST_COMMENT

@register.filter_function
def isReplyPostComment(message):
    return message.type==Message.REPLY_POST_COMMENT

@register.filter_function
def isBlogComment(message):
    return message.type==Message.BLOG_COMMENT

@register.filter_function
def isReplyBlogComment(message):
    return message.type==Message.REPLY_BLOG_COMMENT

@register.filter_function
def getSchoolList(openSchoolList):
    schoolList = openSchoolList.split(' ')
    return schoolList