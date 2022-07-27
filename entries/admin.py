from .models import EntryCategory, CaseEntry
from django.contrib import admin
from django import utils
import core


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'id']
    exclude = []


@admin.register(CaseEntry)
class CaseEntryAdmin(admin.ModelAdmin):
    # raw_id_fields = ['category']
    list_display = ['compact_datetime', 'matter', 'category', 'description', 'time_spent']
    exclude = []

    def get_form(self, request, obj=None, **kwargs):
        # here insert/fill the current user name or id from request
        CaseEntry.added_by = request.user
        CaseEntry.modified_by = request.user
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()

    # def get_changeform_initial_data(self, request):
    #     return {'created_by': request.user, 'modified':utils.timezone.now()}
