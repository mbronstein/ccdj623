from django.contrib import admin
from .models import KbEntryCategory, KbEntry


@admin.register(KbEntryCategory)
class KbEntryCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'type', 'description', 'id']
    ordering = ["name"]
    search_fields = ["name", "description"]


@admin.register(KbEntry)
class KbEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'notes', 'slug','tags']
    list_filter = ["category"]
    # ordering = ["due_date"]
    # search_fields = ["title"]