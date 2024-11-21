from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from .models import Register
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
import time

def ffa(request):
    return render(request,"ffa8975.html")
    
# Create your views here.
@login_required(login_url= "/")
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request,"Kullanıcı adı veya Parola Hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yapıldı.")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)




def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        
        newUser = User(first_name = first_name,
                       last_name = last_name,
                       username = username,
                       email = email)
        newUser.set_password(password)
        newUser.save()
        messages.success(request,"Başarıyla Kayıt Olundu")
        return redirect("index")
    return render(request,"register.html",context)

