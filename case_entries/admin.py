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
    list_display = [compact_datetime, 'matter','category', 'title', 'notes','timespent', 'created_by', 'modified']

    # def get_changeform_initial_data(self, request):
    #     return {'created_by': request.user, 'modified':utils.timezone.now()}

    def compact_datetime(self, obj):
        return core.utils.compact_dow_datetime(obj)
