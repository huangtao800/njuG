from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from njuG.models import Post
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request, 'njuG/index.html');


def post(request):
	from django.utils import timezone
	if(request.method == 'POST' and request.user.is_authenticated()):
		print request.user.username
		try:
# 			content = request.POST['content'];
# 			post = Post(user=request.user, content=content, time=timezone().now)
# 			post.save()
			responseDict = {'result':1, 'msg':''}
			return JsonResponse(responseDict)
		except Exception as e:
			responseDict = {'result':0,'msg': e.message}
			return JsonResponse(responseDict)
	else:
		return JsonResponse({'result':0,'msg':'user not login'})
		