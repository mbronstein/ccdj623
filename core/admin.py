from django.contrib import admin
from .models import Code


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    fields = ['title', 'model', 'field_name', 'description']
    list_display = ['title', "model", 'field_name', 'id']
    ordering = ['title', 'model', 'field_name']
    list_filter = ['model', 'field_name']