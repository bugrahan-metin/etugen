from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
                  "yazar",
                  "title",
                  "content",
                  "source",
                  "imageOne",
                  "descriptionOne",
                  "imageTwo",
                  "descriptionTwo",
                  "imageThree",
                  "descriptionThree",
                  ]
        