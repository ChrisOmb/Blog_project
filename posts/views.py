from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_create(request):
    return render(request, 'posts/create_post.html')

def post_detail(request):
    return HttpResponse('<h1>Blog details</h1>')

def post_list(request):
    return HttpResponse('<h1>list of posts</h1>')

def post_update(request):
    return HttpResponse("<h1>Updates Done</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete post</h1>")