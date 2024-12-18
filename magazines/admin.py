from django.contrib import admin
from .models import Magazine
# Register your models here.

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title"]
    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Magazine
