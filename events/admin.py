from django.contrib import admin
from events.models import Event, EventCategory
from django.utils import timezone


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['compact_start_datetime', 'title', 'matter', 'category', 'length','status']
    exclude = ["created", "modified", "added_by", "modified_by", ]
    list_filter = ['category', 'status']
    search_fields = ["title"]
    ordering = ['start_datetime']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'id')
    exclude = ["created", "modified", "added_by", "modified_by", ]
    list_filter = ['type']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()