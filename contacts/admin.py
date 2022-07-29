from django.contrib import admin
from .models import AsContact
from import_export import resources


@admin.register(AsContact)
class AsContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'id']
    ordering = ['name', ]
    exclude = ["created", "modified", "added_by", "modified_by", ]

# app/admin.py


class AsContactResource(resources.ModelResource):
    class Meta:
        model = AsContact
