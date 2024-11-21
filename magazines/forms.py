from django import forms
from .models import Magazine

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = [
            "author",
            "ıssn",
            "e_ıssn",
            "image",
            "file",
            "title",
            "about",
            "first_create",
        ]