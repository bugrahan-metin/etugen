from django.contrib import admin

from .models import Article

# Register your models here.
# aşağıdaki kod sayesinde models içinde yaptığımız fonksiyonu buraya da taşımış olduk
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]
    # yukarıdaki kod sayesinde article isminin yanında author ve cd yi de gösterdik
    list_display_links = ["title","created_date"]
    # yukardaki kod sayesinde cd ye basınca da article a gitmeyi sağladık
    search_fields = ["title"]
    # title bilgisine gör ebir arama çubuğu oluşturduk

    list_filter = ["created_date"]
    # cd ye göre sağ tarafta bir süzgeç yapmış olduk
    class Meta:
        model = Article
