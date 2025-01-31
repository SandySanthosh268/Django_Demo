from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    blog_title = "Looking for some feedback for this rejected track technology  233445"
    return render(request,'index.html', {'blog_title': blog_title})
 
def post(request):
    return render(request,'detail.html')


def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("this is the new url")