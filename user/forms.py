from django import forms
from django.contrib.auth.models import AbstractBaseUser
from uuid import uuid4
from .models import Register

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget= forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["first_name",
                  "last_name",
                  "username",
                  "password",
                  "confirm",
                  "email",
                  ]
        widgets = {
        'password': forms.PasswordInput(),
        'confirm' : forms.PasswordInput(),
    }
    
    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Uyuşmuyor.")
        values = {
            "first_name" : first_name,
            "last_name":last_name,
            "username": username,
            "password": password,
            "confirm":confirm,
            "email":email,
        }
        return values
    
