from django.contrib import admin
from .models import KbEntryCategory, KbEntry


@admin.register(KbEntryCategory)
class KbEntryCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", 'type', 'description', 'id']
    ordering = ["title"]
    search_fields = ["title", "description"]
    exclude = ["created", "modified", "added_by", "modified_by", ]


@admin.register(KbEntry)
class KbEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']
    list_filter = ["category"]
    exclude = ["created", "modified", "added_by", "modified_by", ]
    # ordering = ["due_date"]
    # search_fields = ["title"]
