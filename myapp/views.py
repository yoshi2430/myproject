from http.client import HTTPResponse
from django.shortcuts import render
from .models import Post

def frontpage(request):
  posts = Post.objects.all()
  return render(request, "myapp/frontpage.html", {"posts": posts}) 