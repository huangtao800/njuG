from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from njuG.models import Post, Like, Comment, Picture, Blog, BlogComment
from django.views.generic import CreateView, DeleteView, ListView
from django.http import JsonResponse, HttpResponseRedirect
from django.utils import timezone
from njuG.forms.myForms import BlogForm

# Create your views here.
def index(request):
	if(request.user.is_authenticated()):
		posts = Post.objects.all()
		likedPosts = [x.post.id for x in Like.objects.filter(user=request.user)]
		context = {'posts': posts, 'likedPosts':likedPosts}
	else:
		posts = Post.objects.all()
		context = {'posts': posts}	
	return render(request, 'njuG/index.html', context)


def post(request):
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
		return JsonResponse({'result':0, 'msg':'user not login'})
	
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
		return JsonResponse({'result':0, 'msg':'user not login'})
	
def postComment(request):
	if(request.method=='POST' and request.user.is_authenticated()):
		try:
			postid = request.POST['postid']
			content = request.POST['content']
			post = Post.objects.get(pk=postid)
 			comment = Comment(content=content, user=request.user, post=post, time=timezone.now())
 			comment.save()
 			responseDict={'result':1, 'msg':''}
 			return JsonResponse(responseDict)
 		except Exception as e:
 			print e.message
 			responseDict = {'result':0, 'msg':e.message}
 			return JsonResponse(responseDict)
 	else:
 		return JsonResponse({'result':0, 'msg':'user not login'})
 	
 	
class PictureListView(ListView):
    model = Picture

    def render_to_response(self, context, **response_kwargs):
        files = [ serialize(p) for p in self.get_queryset() ]
        data = {'files': files}
        response = JsonResponse(data)
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


def discussion(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request, 'njuG/discussion.html', context)

@login_required
def postDiscussion(request):
	if(request.method=='POST'):
		form = BlogForm(request.POST)
		print form.errors
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			isAnonymous = form.cleaned_data['isAnonymous']
			user = request.user
			blog = Blog(title=title,content=content,isAnonymous=isAnonymous,user=user, time=timezone.now())
			blog.save()
			return HttpResponseRedirect("/njuG/discussion")
	else:
		form = BlogForm()
	return render(request, 'njuG/postDiscussion.html',{'form': form})

def viewDiscussion(request, id):
	if(request.method=='GET'):
		blog = Blog.objects.get(pk=id)
		blogComments = blog.blogcomment_set.all()
		context = {'blog':blog, 'blogComments': blogComments}
		return render(request, 'njuG/viewDiscussion.html', context)

@login_required
def commentBlog(request):
	if(request.method=='POST'):
		blogid = request.POST['blogid']
		content = request.POST['content']
		user = request.user
		blog = Blog.objects.get(pk=blogid)
		blogComment = BlogComment(content=content, user=user, blog=blog)
		blogComment.save()
		return JsonResponse({'result':1, 'msg':''})

@login_required
def replyBlogComment(request):
	if(request.method=='POST'):
		blogid = request.POST['blogid']
		commentid = request.POST['commentid']
		masterCommentid = request.POST['masterCommentid']
		print masterCommentid
		content = request.POST['content']
		user = request.user
		blog = Blog.objects.get(pk=blogid)
		replyTo = BlogComment.objects.get(pk=commentid)
		masterComment = BlogComment.objects.get(pk=masterCommentid)
		blogComment = BlogComment(content=content, user=user, blog=blog, replyTo=replyTo, masterComment=masterComment)
		blogComment.save()
		return JsonResponse({'result':1, 'msg':''})