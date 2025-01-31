from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.
def index(request):
    blog_title = "Latest Posts "
    post=[
        {'id':1,'title':'post 1' , 'content':'content of post 1'},
        {'id':2,'title':'post 2' , 'content':'content of post 2'},
        {'id':3,'title':'post 3' , 'content':'content of post 3'},
        {'id':4,'title':'post 4' , 'content':'content of post 4'},
    ]
    return render(request,'index.html', {'blog_title': blog_title, 'posts':post})
 
def detail(request,post_id):
    return render(request,'detail.html')


def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("this is the new url")