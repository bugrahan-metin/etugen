from django.db import models


# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=25,verbose_name="İsim")
    last_name = models.CharField(max_length=25,verbose_name="Soyisim",blank=True,null=True)
    username = models.CharField(max_length=20,verbose_name="Kullanıcı Adı")
    password = models.CharField(max_length=40,verbose_name="Parola")
    confirm = models.CharField(max_length=40,verbose_name="Parolayı Onayla")
    email = models.EmailField(max_length=60,verbose_name="Email")




