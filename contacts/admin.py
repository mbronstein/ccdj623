from django.contrib import admin
from .models import AsContact
from import_export import resources


@admin.register(AsContact)
class AsContactAdmin(admin.ModelAdmin):
    # fields = ['name', 'model', 'field_name', 'description', 'id']
    list_display = ['name', 'email']
    ordering = ['name', ]


# app/admin.py


class AsContactResource(resources.ModelResource):
    class Meta:
        model = AsContact
