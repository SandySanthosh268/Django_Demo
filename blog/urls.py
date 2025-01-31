from django.urls import path
from . import views

app_name= 'blog'

urlpatterns=[
     path("post/",views.post,name="detail"),
    path("blog/", views.index, name="index"),
   
    path("new_url", views.new_url_view, name="new_url"),
    path("old_url", views.old_url_redirect, name="old_url"),



]