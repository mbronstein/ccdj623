from django.contrib import admin
from events.models import Event, EventCategory
from django.utils import timezone


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['compact_dow_datetime', 'length', 'title', 'matter', 'assigned_to', 'status']
    readonly_fields = ['compact_dow_datetime']
    list_editable = ['title','status', 'length', 'assigned_to']
    fields = ['datetime', 'length', 'title', 'matter', 'category', 'status', 'attendees', 'location',
              'location_url', 'assigned_to', 'notes']
    exclude = ["modified', 'created", 'added_by', 'modified_by', 'description', 'slug', 'tag']
    list_filter = ['category', 'status']
    search_fields = ["title"]

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
