from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from magazines.models import Magazine
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
# Create your views here.

def isAdmin(user):
    return user.is_superuser

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        
        return render(request,"articles.html",{"articles":articles})
    
    
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def index(request):
    last_magazines = Magazine.objects.order_by("created_date")[:2]

    context = {
        "last_magazines": last_magazines    
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

@login_required
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request,"dashboard.html",context)

@user_passes_test(isAdmin)
def dashart(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request,"dashart.html",context)

@user_passes_test(isAdmin)
def addArticle(request):
    art = "Makale"
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit= False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("article:dashart")


    return render(request,"addarticle.html",{"form":form,"art":art})

def detail(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    keywords = article.keywords.split(",")
    return render(request,"detail.html",{"article":article,"keywords":keywords})




@user_passes_test(isAdmin)
def updateArticle(request,id):

    art = "Makale"
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit= False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("article:dashart")

    return render(request,"update.html",{"form":form,"art":art})

