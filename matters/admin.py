from django.contrib import admin
from .models import MatterType, Matter



@admin.register(MatterType)
class MatterTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'id']
    exclude = [ "created", "modified", "added_by", "modified_by", ]


@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', ]
    fields = ["title", "type", "description", "files_foldername", "case_id" ]
    exclude = ["notes", "created", "modified", "added_by", "modified_by", ]
    list_filter = ['type']
    search_fields = ['title']


