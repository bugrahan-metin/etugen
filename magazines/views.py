from django.shortcuts import render,redirect,get_object_or_404
from .forms import MagazineForm
from .models import Magazine
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
def isAdmin(user):
    return user.is_superuser
def magazines(request):
    keyword = request.GET.get("keyword")

    if keyword:
        magazines = Magazine.objects.filter(title__contains = keyword)
        return render(request,"magazines.html",{"magazines":magazines})
    
    magazines = Magazine.objects.all()
    return render(request,"magazines.html",{"magazines":magazines})

@user_passes_test(isAdmin)
def addMagazine(request):
    art = "Dergi"
    form = MagazineForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()

        messages.success(request,"Dergi Başarıyla Oluşturuldu")
        return redirect("magazines:dashmag")
    
    return render(request,"addarticle.html",{"form":form,"art":art})

@user_passes_test(isAdmin)
def dashmag(request):
    magazines = Magazine.objects.all()
    context = {
        "magazines": magazines
    }
    return render(request,"dashmag.html",context)

def detail(request,id):
    magazine = get_object_or_404(Magazine,id=id)
    return render(request,"magdetail.html",{"magazine":magazine})

@user_passes_test(isAdmin)
def updateMagazine(request,id):
    art = "Dergi"
    magazine = get_object_or_404(Magazine,id = id)
    form = MagazineForm(request.POST or None, request.FILES or None, instance = magazine)
    if form.is_valid():
        form.save()

        messages.success(request,"Dergi Başarıyla Güncellendi")
        return redirect("magazines:dashmag")
    return render(request,"update.html",{"form":form,"art":art})