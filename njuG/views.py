from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from njuG.models import Post, Like
from django.http import JsonResponse

# Create your views here.
def index(request):
	if(request.user.is_authenticated()):
		posts = Post.objects.all()
		context = {'posts': posts}
	else:
		posts = Post.objects.all()
		context = {'posts': posts}	
	return render(request, 'njuG/index.html', context)


def post(request):
	from django.utils import timezone
	if(request.method == 'POST' and request.user.is_authenticated()):
		try:
			postContent = request.POST['content']
			post = Post(user=request.user, content=postContent, time=timezone.now())
			post.save()
			responseDict = {'result':1, 'msg':''}
			return JsonResponse(responseDict)
		except Exception as e:
			print e.message
			responseDict = {'result':0,'msg': e.message}
			return JsonResponse(responseDict)
	else:
		return JsonResponse({'result':0,'msg':'user not login'})
	
def likePost(request):
	if(request.method=='POST' and request.user.is_authenticated()):
		try:
			postid = request.POST['postid']
			post = Post.objects.get(pk=postid)
			user = request.user
			like = Like(user=user, post = post)
			like.save()
			post.likes = post.likes+1;
			post.save();
			responseDict = {'result':1, 'msg': 1}
			return JsonResponse(responseDict)
		except Exception as e:
			print e.message
			responseDict = {'result':0, 'msg':e.message}
			return JsonResponse(responseDict)
	else:
		return JsonResonse({'result':0, 'msg':'user not login'})
	
def notLikePost(request):
	if(request.method=='POST' and request.user.is_authenticated()):
		try:
			postid = request.POST['postid']
			post = Post.objects.get(pk=postid)
			like = Like.objects.get(user=request.user, post=post)
			like.delete()
			post.likes = post.likes-1;
			post.save();
			responseDict = {'result':1, 'msg':''}
			return JsonResponse(responseDict)
		except Exception as e:
			print e.message
			responseDict = {'result':0, 'msg':e.message}
			return JsonResponse(responseDict)
	else:
		return JsonResonse({'result':0, 'msg':'user not login'})