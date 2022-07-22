from django.contrib import admin
from events.models import Event, EventCategory



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['compact_start_datetime', 'title', 'category', 'matter', 'length', 'location']
    list_filter = ["matter", 'category']
    ordering = ["start_datetime"]
    search_fields = ["title"]


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'id')
    ordering = ['name']
