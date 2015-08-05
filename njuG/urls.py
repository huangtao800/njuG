from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    url(r'^likePost', views.likePost, name='likePost'),
    url(r'^notLikePost', views.notLikePost, name='notLikePost'),
    url(r'^postComment', views.postComment, name='postComment'),
    url(r'^replyPostComment', views.replyPostComment, name='replyPostComment'),
    
    
    url(r'^postUploadImg', views.postUploadImg, name='postUploadImg'),
    url(r'^deletePostImg/(?P<pk>[0-9]+)/$', views.deletePostImg, name='deletePostImg'),

    #need to change view
    
    url(r'^discussion/', views.discussion, name="discussion"),
    url(r'^postDiscussion/', views.postDiscussion, name="postDiscussion"),
    url(r'^editDiscussion/(?P<id>[0-9]+)/$', views.editDiscussion, name="editDiscussion"),
    url(r'^deleteDiscussion/$', views.deleteDiscussion, name="deleteDiscussion"),
    url(r'^viewDiscussion/(?P<id>[0-9]+)/$', views.viewDiscussion, name="viewDiscussion"),
    url(r'^commentBlog/', views.commentBlog, name="commentBlog"),
    url(r'^replyBlogComment/', views.replyBlogComment, name="replyBlogComment"),
    
    url(r'^profile/', views.profile, name="profile"),
    url(r'^postAvatar/', views.postAvatar, name="postAvatar"),
    
    url(r'^activity/', views.activity, name="activity"),
    url(r'^createActivity/', views.createActivity, name="createActivity"),
    url(r'^viewActivity/(?P<id>[0-9]+)/$', views.viewActivity, name="viewActivity"),
    
    url(r'^postActivity/', views.postActivity, name="postActivity"),
    
    url(r'^home/message/$', views.message, name="message"),
    url(r'^home/$', views.home, name="myHome"),
    url(r'^home/(?P<id>[0-9]+)/$', views.home, name="home"),
    url(r'^home/myDiscussion$', views.myDiscussion, name="myDiscussion"),
    url(r'^home/(?P<id>[0-9]+)/myDiscussion$', views.myDiscussion, name="hisDiscussion"),
    
    url(r'^setMessageRead/$', views.setMessageRead, name="setMessageRead"),
    url(r'^sendMessage/$', views.sendMessage, name="sendMessage"),
    
    url(r'^searchUsers/$', views.searchUsers, name="searchUsers"),
    url(r'^poll/$', views.poll, name="poll"),
]