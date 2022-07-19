from django.contrib import admin
from .models import MatterType, Matter


@admin.register(MatterType)
class MatterTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'id']


@admin.register(Matter)
class MatterAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'files_foldername']
