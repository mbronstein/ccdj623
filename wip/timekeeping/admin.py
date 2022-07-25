from django.contrib import admin
from .models import Code


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    fields = ['name', 'model', 'field_name', 'description']
    list_display = ['name', "model", 'field_name', 'id']
    ordering = ['name', 'model', 'field_name']
    list_filter = ['model', 'field_name']