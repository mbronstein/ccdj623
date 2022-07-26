from django.contrib import admin
from events.models import Event, EventCategory



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['compact_start_datetime', 'title','matter',  'category',  'length', 'location']
    exclude = ["created", "modified", "added_by", "modified_by", ]
    list_filter = [ 'category']
    ordering = ["start_datetime"]
    search_fields = ["title"]


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'id')
    exclude = ["created", "modified", "added_by", "modified_by", ]
    ordering = ['name']
    list_filter = ['type']