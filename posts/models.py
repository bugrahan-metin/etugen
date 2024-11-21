from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name = "Paylaşan")
    yazar = models.CharField(max_length=25,verbose_name= "Yazar İsmi",blank=True,null=True)
    date = models.DateField(verbose_name= "Yazım Tarihi",blank=True,null=True)
    source = RichTextField(verbose_name = "Kaynakça",default="")
    imageOne = models.ImageField(blank=True,null=True, verbose_name = "Ek 1")
    descriptionOne = models.CharField(max_length=400, verbose_name="Ek 1 Açıklama",blank = True, null=True)
    imageTwo = models.ImageField(blank=True,null=True, verbose_name = "Ek 2")
    descriptionTwo = models.CharField(max_length=400, verbose_name="Ek 2 Açıklama",blank = True, null=True)
    imageThree = models.ImageField(blank=True,null=True, verbose_name = "Ek 3")
    descriptionThree = models.CharField(max_length=400, verbose_name="Ek 3 Açıklama",blank = True, null=True)

    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField(verbose_name= "İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Oluşturulma Tarihi")
    
    def __str__(self):
        return self.title
