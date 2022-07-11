from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from blog.models import Categorie

# Create your views here.
def home(request):
    post=Post.objects.all()[:11]
    print(category)
    data={
        'posts':post,
    }
    return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    print(post)
    return render(request,'posts.html',{'post':post})