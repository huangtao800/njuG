from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    url(r'^likePost', views.likePost, name='likePost'),
    url(r'^notLikePost', views.notLikePost, name='notLikePost'),
    url(r'^postComment', views.postComment, name='postComment'),
    url(r'^uploadPicView$', views.PictureListView.as_view(), name='uploadPicView'),
    url(r'^uploadPicNew/(?P<id>[0-9]+)/$', views.PictureListView.as_view(), name='uploadPicNew'),
    #need to change view
    
    url(r'^discussion/', views.discussion, name="discussion"),
    url(r'^postDiscussion/', views.postDiscussion, name="postDiscussion"),
    url(r'^viewDiscussion/(?P<id>[0-9]+)/$', views.viewDiscussion, name="viewDiscussion"),
]