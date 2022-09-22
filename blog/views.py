from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def creat1000(request):

    me=User.objects.get(username='admin')
    for i in range(100):
        post=Post.objects.create(author=me, title=f'Sample title from {i}', text=f'Test From{i}')
        post.publish()

    return HttpResponse("sss")