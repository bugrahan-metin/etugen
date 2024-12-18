from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Magazine(models.Model):
    author = models.CharField(max_length=50,verbose_name="Yayımcı",blank=True,null=True)
    ıssn = models.CharField(max_length=100,verbose_name = "ISSN", blank= True,null = True)
    e_ıssn = models.CharField(max_length=100,verbose_name = "e-ISSN", blank = True, null= True)
    image = models.ImageField(blank=True,null=True, verbose_name = "Derginin Kapağı")
    file = models.FileField(blank= True, null = True, verbose_name = "Dergi")
    title = models.CharField(max_length=150, verbose_name="Derginin İsmi")
    about = RichTextField(verbose_name="Hakkında")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    first_create = models.DateField(verbose_name="İlk Çıkış Tarihi")

    def __str__(self):
        return self.title
    
