from .models import EntryCategory, CaseEntry
from django.contrib import admin
from django import utils
import core


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'id']


@admin.register(CaseEntry)
class CaseEntryAdmin(admin.ModelAdmin):
    # raw_id_fields = ['category']
    list_display = ['compact_datetime', 'matter', 'category', 'title', 'notes', 'time_spent', 'modified']

    # def get_changeform_initial_data(self, request):
    #     return {'created_by': request.user, 'modified':utils.timezone.now()}
