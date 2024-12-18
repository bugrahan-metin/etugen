from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
import time
# Create your views here.
def isAdmin(user):
    return user.is_superuser




def posts(request):
    posts = Post.objects.all()
    return render(request,"posts.html",{"posts":posts})

@login_required
def addPost(request):
    post = "Gönderi"
    form = PostForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        post = form.save(commit= False)
        post.author = request.user
        post.save()

        messages.success(request,"Gönderin Paylaşıldı")
        return redirect("posts:dashpost")

    return render(request,"addpost.html",{"form":form,"post":post})
@login_required
def dashpost(request):
    if request.user.is_superuser :
        posts = Post.objects.all()


    else:
        posts = Post.objects.filter(author = request.user)
    context = {
    "posts":posts
    }
    return render(request,"dashpost.html",context)
    

def detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,"postdetail.html",{"post":post})

@user_passes_test(isAdmin)
def deletePost(request,id):
    post = get_object_or_404(Post,id=id)
    messages.success(request,"Gönderi Başarıyla Silindi")
    return redirect("posts:dashpost")

