from django.contrib import admin
from .models import MatterType, Matter


@admin.register(MatterType)
class MatterTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'id']
    exclude = ["assigned_to", "created", "modified", "added_by", "modified_by", ]


@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'files_foldername']
    fields = ["title", "type", "files_foldername", "case_id" ]
    exclude = ["description", "notes", "assigned_to", "created", "modified", "added_by", "modified_by", ]


