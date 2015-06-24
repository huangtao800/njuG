from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.post, name='post'),
    url(r'^likePost', views.likePost, name='likePost'),
    url(r'^notLikePost', views.notLikePost, name='notLikePost'),
    url(r'^postComment', views.postComment, name='postComment'),
]