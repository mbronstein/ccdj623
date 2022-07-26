from django.contrib import admin
from .models import AsContact
from import_export import resources


@admin.register(AsContact)
class AsContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'email']
    ordering = ['title', ]


# app/admin.py


class AsContactResource(resources.ModelResource):
    class Meta:
        model = AsContact
