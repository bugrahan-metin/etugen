from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["publisher",
                  "publisher_detail",
                  "keywords",
                  "source",
                  "article_language",
                  "article_type",
                  "title",
                  "content",
                  "article_file"]
        widgets = {
            'language': forms.Select(choices=Article.LANGUAGE_CHOICES),
        }