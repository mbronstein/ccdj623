from .models import EntryCategory, CaseEntry
from django.contrib import admin
from django.utils import timezone
from core.utils import compact_datetime
from admin_auto_filters.filters import AutocompleteFilterFactory

MatterFilter = AutocompleteFilterFactory('Matter', 'matter')
CategoryFilter = AutocompleteFilterFactory('Category', 'category')


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['compact_datetime', 'title', 'type', 'id']
    exclude = ["created", "modified", "added_by", "modified_by", "description" ]
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = request.user
        obj.modified_by = request.user
        obj.save()


@admin.register(CaseEntry)
class CaseEntryAdmin(admin.ModelAdmin):
    # raw_id_fields = ['category']
    list_display = ['compact_dow_datetime', 'matter', 'category', 'description', 'time_spent']
    exclude = ["created", "modified", "added_by", "modified_by", "description", 'slug']
    list_editable = ['category', 'time_spent']
    list_filter = [MatterFilter, CategoryFilter, 'datetime']
    fields = ['matter', 'datetime', 'category',  'title', 'notes', 'time_spent', 'tags', 'status', 'priority']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()

    # def get_changeform_initial_data(self, request):
    #     return {'created_by': request.user, 'modified':utils.timezone.now()}urls
