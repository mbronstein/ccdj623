from django.contrib import admin
from .models import KbEntryCategory, KbEntry
from django.utils import timezone


@admin.register(KbEntryCategory)
class KbEntryCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", 'type', 'description', 'id']
    ordering = ["title"]
    search_fields = ["title", "description"]
    exclude = ["created", "modified", "added_by", "modified_by", ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()


@admin.register(KbEntry)
class KbEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']
    list_filter = ["category"]
    exclude = ["created", "modified", "added_by", "modified_by", ]
    # ordering = ["due_date"]
    # search_fields = ["title"]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()
