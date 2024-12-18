from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'İngilizce'),
        ('ES', 'İspanyolca'),
        ('FR', 'Fransıca'),
        ('DE', 'Almanca'),
        ('TR', 'Türkçe'),
        # Diğer diller burada eklenebilir
    ]
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yayıncı")
    publisher = models.CharField(max_length=50, verbose_name="Yazar İsmi",blank=True,null=True)
    publisher_detail= models.CharField(max_length=50, verbose_name="Yazar Detayları",blank=True,null=True)
    keywords = models.CharField(max_length=500,verbose_name="Anahtar Kelimeler",blank=True,null=True)
    source = RichTextField(verbose_name="Kaynakça",default="")
    article_language = models.CharField(max_length=2,choices=LANGUAGE_CHOICES,default="TR",verbose_name="Makale Dili")
    #foreignkey kullanarak author bilgisini kayıtlı kullanuculardan çekmesini istedik
    # models.CASCADE kullanarak eğer kullanıcı silinirse ona ait articleların da silinmesini sağladık
    # verbose_name methodunu kullanarakj değişken ismini belirledik
    article_type = models.CharField(max_length=50,verbose_name="Makale Türü",blank=True,null=True)
    title = models.CharField(max_length= 50, verbose_name= "Başlık")
    # max_lenght kullanarak kaç karakterlik bir yazı olacağını belirledik
    content = RichTextField(verbose_name="Özet")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    # bu kod sayesinde uygulamanın tarihi otomatik olarak alabilmesini sağladık
    #article ismini title olarak göstermek için özel bir fonksiyon
    article_file = models.FileField(blank = True,null = True, verbose_name="Makalenin Kendisi")
    
    def __str__(self):
        return self.title
    
