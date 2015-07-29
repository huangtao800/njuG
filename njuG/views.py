from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.conf import settings

from njuG.models import Post, Like, Comment, Blog, BlogComment, Image, Profile
from django.views.generic import CreateView, DeleteView, ListView
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.utils import timezone
from njuG.forms.myForms import BlogForm, ProfileForm
from allauth.account.signals import user_signed_up

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

# @login_required
def post(request):
	if(request.method == 'POST' and request.user.is_authenticated()):
		try:
			postContent = request.POST['content']
			imgPkList = request.POST.getlist('imgPkList[]')
			post = Post(user=request.user, content=postContent, time=timezone.now())
			for idx, val in enumerate(imgPkList):
				attrName = "img" + str(idx+1);
				img = get_object_or_404(Image, pk=val)
				setattr(post, attrName, img)
				print img.pk
			
			post.save()
			responseDict = {'result':1, 'msg':''}
			return JsonResponse(responseDict)
		except Exception as e:
			print e.message
			responseDict = {'result':0,'msg': e.message}
			return JsonResponse(responseDict)
	else:
		return JsonResponse({'result':0,'msg':'user not login'})

# @login_required	
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

# @login_required	
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

# @login_required	
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
 	

# @login_required
def postUploadImg(request):
	from django.core.files.uploadedfile import UploadedFile
	from sorl.thumbnail import get_thumbnail
	if request.method == 'POST' and request.user.is_authenticated():
		if request.FILES == None:
			return HttpResponseBadRequest('Must have files attached!')
		
		file = request.FILES[u'files[]']
		filename = file.name
		filesize = file.size
		
		image = Image()
		image.file = file
		image.user = request.user
		image.save()
		
		file_delete_url = '/njuG/deletePostImg/'
		file_url = '/'
		
		im = get_thumbnail(image, "80x80", quality=50)
		thumb_url = im.url
		
		imgList = []
		imgList.append({"name": filename,
						"size": filesize,
						"url": file_url,
						"imgPk": image.pk,
						"thumbnail_url": thumb_url,
						"deleteUrl": file_delete_url + str(image.pk) + '/',
						"deleteType": "POST"})
		
		return JsonResponse({"files": imgList});
	
def deletePostImg(request, pk):
	if request.method == 'POST':
		image = get_object_or_404(Image, pk=pk)
		if(image.user.username == request.user.username):
			image.delete()
			return HttpResponse(str(pk))
		else:
			return HttpResponseBadRequest('You can only delete your images')
	else:
		return HttpResponseBadRequest('Only POST accepted')


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

@receiver(user_signed_up)
def createProfile(sender, **kwargs):
    user = kwargs['user']
    profile = Profile(user=user, nickName=user.username)
    profile.save()
	
@login_required
def profile(request):
	if(request.method == "GET"):
		profile = request.user.profile
		profileForm = ProfileForm(initial={'nickName': profile.nickName, 'school':profile.school, 'role': profile.role})
		if(profile.hasAvatar):
			avatar_path = "/static/img/avatar/" + request.user.username
		else:
			avatar_path = "/static/img/avatar/" + "Default-Avatar.jpg"
		return render(request, 'njuG/profile.html', {'form': profileForm,'avatar_path': avatar_path})
	else:
		profileForm = ProfileForm(request.POST)
		print profileForm.errors
		if profileForm.is_valid():
			profile = request.user.profile
			profile.nickName = profileForm.cleaned_data['nickName']
			profile.school = profileForm.cleaned_data['school']
			profile.degree = profileForm.cleaned_data['degree']
			profile.role = profileForm.cleaned_data['role']
			profile.save()
			return render(request, 'njuG/profile.html', {'form': profileForm})

@login_required
def postAvatar(request):
	from PIL import Image as PILImage
	import cStringIO, base64, re
	
	if(request.method=='POST'):
		x = int(float(request.POST['x']))
		y = int(float(request.POST['y']))
		width = int(float(request.POST['width']))
		height = int(float(request.POST['height']))
		imgContent = request.POST['imgContent']
		imgData = re.sub('^data:image/.+;base64,', '', imgContent)
		imgName = request.POST['imgName']
		username = request.user.username
		
		pic = cStringIO.StringIO()
		image_string = cStringIO.StringIO(base64.b64decode(imgData))
		image = PILImage.open(image_string)
		image.save(settings.AVATAR_ORIGIN_PATH + username, image.format, quality = 100)
		pic.seek(0)
		
		largeAvatar = image.crop((x,y,x+width,y+height))
		size = (150, 150)
		largeAvatar.thumbnail(size)
		
		largeAvatar.save(settings.AVATAR_PATH+username, image.format)
		request.user.profile.hasAvatar = True
		request.user.profile.save()
		return JsonResponse({'result': 1, 'msg':''})
	
def activity(request):
	if(request.method=='GET'):
		return render(request, 'njuG/activity.html')

@login_required
def home(request, **kwargs):
	if(request.method=='GET'):
		return render(request, 'njuG/home.html')
				