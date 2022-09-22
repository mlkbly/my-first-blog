from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def creat1000(request):
    me=User.objects.get(username='admin')
    for i in range(100):
        Post.objects.create(author=me, title=f'Sample title{i}', text=f'Test{i}')
    return HttpResponse("sss")