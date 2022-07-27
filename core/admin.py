from django.contrib import admin
from .models import Code
from django.utils import timezone


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    # fields = ['title', 'model', 'field_name', 'description', id]
    list_display = ['title', "model", 'field_name', 'id']
    ordering = ['title', 'model', 'field_name']
    list_filter = ['model', 'field_name']
    exclude = ["created", "modified", "added_by", "modified_by", ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()