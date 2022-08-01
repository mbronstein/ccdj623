from django.contrib import admin
from .models import AsContact, AsParticipant

from import_export import resources


@admin.register(AsContact)
class AsContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'id']
    ordering = ['name', ]
    exclude = ["created", "modified", "added_by", "modified_by", ]


# app/admin.py


@admin.register(AsParticipant)
class AsParticipantAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'org_name', 'phone1_area_code', 'phone1', 'email', 'id']
    list_editable = ['phone1_area_code', 'phone1']
    ordering = ['last_name', 'first_name', 'org_name', ]
    exclude = ["created", "modified", "added_by", "modified_by", ]
    search_fields = ['last_name', 'org']
