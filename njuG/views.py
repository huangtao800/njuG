from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from njuG.models import Post

# Create your views here.
def index(request):
	return render(request, 'njuG/index.html');

def post(request):
	from django.utils import timezone
	if(request.POST):
		content = request.POST['content'];
		post = Post(user=request.user, content=content, time=timezone().now)