from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'njuG/index.html');

def post(request):
	if(request.POST):
		content = request.POST['content'];
		