# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from njuG.models import Post, Like, Comment, Blog, BlogComment, Image, Profile, Message, Activity
from django.views.generic import CreateView, DeleteView, ListView
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.utils import timezone
from njuG.forms.myForms import BlogForm, ProfileForm, ActivityForm
from allauth.account.signals import user_signed_up
from . import utils

# Create your views here.
def index(request):
	post_list = Post.objects.all()
	paginator = Paginator(post_list, 8)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
		
	return render(request, 'njuG/index.html', {'posts': posts})

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
			like = Like(user=user, post = post, time=timezone.now())
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
 			
 			target = post.user
 			if target.id != request.user.id:
	 			utils.createMessage(request.user, target, type=Message.POST_COMMENT,
						 post=post, content=content, postComment=comment)
 			return JsonResponse(responseDict)
 		except Exception as e:
 			print e.message
 			responseDict = {'result':0, 'msg':e.message}
 			return JsonResponse(responseDict)
 	else:
 		return JsonResponse({'result':0, 'msg':'user not login'})

# @login_required 	
def replyPostComment(request):
	if(request.method=='POST' and request.user.is_authenticated()):
		postid = request.POST['postid']
		content = request.POST['content']
		commentid = request.POST['commentid']
		
		post = Post.objects.get(pk=postid)
		comment = Comment.objects.get(pk=commentid)
		replyComment = Comment(content=content, user=request.user, post=post, replyTo=comment)
		replyComment.save()
		responseDict={'result':1, 'msg':''}
		
		target1 = post.user	# topic owner
		target2 = comment.user	# comment owner
		if target1.id != request.user.id:
			utils.createMessage(request.user, target1, type=Message.REPLY_POST_COMMENT, 
				post=post, content=content, postComment=replyComment)
			
 		if target1.id != target2.id and target2.id!=request.user.id:
 			utils.createMessage(request.user, target2, type=Message.REPLY_POST_COMMENT, 
				post=post, content=content, postComment=replyComment)
 		return JsonResponse(responseDict)

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
	blog_list = Blog.objects.all()
	paginator = Paginator(blog_list, 10)
	page = request.GET.get('page')
	
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
		
	context = {'blogs': blogs}
	return render(request, 'njuG/discussion.html', context)

@login_required
def postDiscussion(request):
	if(request.method=='POST'):
		form = BlogForm(request.POST)
		print form.errors
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['blogContent']
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
		blog.viewCount+=1
		blog.save()
		context = {'blog':blog, 'blogComments': blogComments}
		return render(request, 'njuG/viewDiscussion.html', context)

@login_required
def commentBlog(request):
	if(request.method=='POST'):
		try:
			blogid = request.POST['blogid']
			content = request.POST['content']
			user = request.user
			blog = Blog.objects.get(pk=blogid)
			blogComment = BlogComment(content=content, user=user, blog=blog, time=timezone.now())
			blogComment.save()
			blog.commentCount+=1
			blog.save()
			
			target = blog.user
			if target.id != request.user.id:
				utils.createMessage(request.user, target, type=Message.BLOG_COMMENT, 
						blog=blog, content=content, blogComment=blogComment)
			return JsonResponse({'result':1, 'msg':''})
		except Exception as e:
			print e.message
			responseDict = {'result':0, 'msg':e.message}
			return JsonResponse(responseDict)

@login_required
def replyBlogComment(request):
	if(request.method=='POST'):
		try:
			blogid = request.POST['blogid']
			commentid = request.POST['commentid']
			masterCommentid = request.POST['masterCommentid']
	# 		print masterCommentid
			content = request.POST['content']
			user = request.user
			blog = Blog.objects.get(pk=blogid)
			replyTo = BlogComment.objects.get(pk=commentid)
			masterComment = BlogComment.objects.get(pk=masterCommentid)
			blogComment = BlogComment(content=content, user=user, blog=blog, replyTo=replyTo, masterComment=masterComment)
			blogComment.save()
			blog.commentCount+=1
			blog.save()
			
			target1 = blog.user
			target2 = replyTo.user
			if target1.id != request.user.id:
				utils.createMessage(request.user, target1, type=Message.REPLY_BLOG_COMMENT, 
								blog=blog, content=content, blogComment=blogComment, masterComment=masterComment)
			if target2.id!=target1.id and target2.id!=request.user.id:
				utils.createMessage(request.user, target2, type=Message.REPLY_BLOG_COMMENT, 
								blog=blog, content=content, blogComment=blogComment, masterComment=masterComment)
			return JsonResponse({'result':1, 'msg':''})
		except Exception as e:
			print e.message
			responseDict = {'result':0, 'msg':e.message}
			return JsonResponse(responseDict)
			

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
			profile.birth_year = profileForm.cleaned_data['birth_year']
			profile.save()
			return JsonResponse({'result':1, 'msg':''})

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
		size = (200, 200)
		largeAvatar.thumbnail(size)
		
		largeAvatar.save(settings.AVATAR_PATH+username, image.format)
		request.user.profile.hasAvatar = True
		request.user.profile.save()
		return JsonResponse({'result': 1, 'msg':''})
	
def activity(request):
	if(request.method=='GET'):
		
		activity_list = Activity.objects.all()
		paginator = Paginator(activity_list, 10)
		page = request.GET.get('page')
		
		try:
			activities = paginator.page(page)
		except PageNotAnInteger:
			activities = paginator.page(1)
		except EmptyPage:
			activities = paginator.page(paginator.num_pages)
			
		context = {'activities': activities}
		return render(request, 'njuG/activity.html',context)

@login_required
def home(request, **kwargs):
	if(request.method=='GET'):
		if('id' in kwargs):
			id = kwargs['id']
			user = User.objects.get(pk=id)
			target = user
			return render(request, 'njuG/home.html', {"target":target})
		else:
			target = request.user
			return render(request, 'njuG/home.html', {"target": target})
				
@login_required
def message(request):
	if(request.method=='GET'):
		target = request.user
		messages = Message.objects.filter(target=request.user)
		return render(request, 'njuG/message.html', {"target": target,"messages":messages})

@login_required
def setMessageRead(request):
	if(request.method=="POST"):
		messageid = request.POST['messageid']
		message = Message.objects.get(pk=messageid)
		if not message.isRead:
			message.isRead = True
			request.user.profile.unreadMessageCount-=1
			if request.user.profile.unreadMessageCount < 0:
				request.user.profile.unreadMessageCount = 0
			message.save()
			request.user.profile.save()
			return JsonResponse({'result': 1, 'msg':''})
		else:
			return JsonResponse({'result': 0, 'msg':''})

@login_required
def createActivity(request):
	if(request.method=='GET'):
		activityForm = ActivityForm()
		return render(request,'njuG/createActivity.html',{'form': activityForm})
	else:
		pass	

def validateSchool(onlyForSchool):
	pass

@login_required
def postActivity(request):
	if(request.method=='POST'):
		form = ActivityForm(request.POST)
		if(form.is_valid()):
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			onlyForSchool = form.cleaned_data['onlyForSchool']
			openToAll = form.cleaned_data['openToAll']
			contact = form.cleaned_data['contact']
			detailContact = form.cleaned_data['detailContact']
			openSchoolList = form.cleaned_data['openSchoolList']
 			
			openSchoolListData = " ".join(openSchoolList)
			print openSchoolListData
			activity = Activity(user=request.user, title=title,content=content,onlyForSchool=onlyForSchool,
							openToAll=openToAll,contact=contact,detailContact=detailContact,
							openSchoolList=openSchoolListData)
			activity.save()
			return JsonResponse({'result': 1, 'msg':''})

def viewActivity(request, id):
	if(request.method=='GET'):
		activity = Activity.objects.get(pk=id)
		return render(request, "njuG/viewActivity.html", {"activity": activity})
	
def sendMessage(request):
	if request.method=='POST' and request.user.is_authenticated():
		messageContent = request.POST['messageContent']
		targetid = request.POST['targetid']
		target = User.objects.get(pk=targetid)
		utils.createMessage(request.user, target, content=messageContent, type=Message.PRIVATE_MESSAGE)
		return JsonResponse({'result': 1, 'msg':''})
	else:
		return JsonResponse({'result': 0, 'msg':'user not login'})
		