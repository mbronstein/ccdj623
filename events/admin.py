from django.contrib import admin
from events.models import Event, EventCategory



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['compact_startdatetime', 'title', 'category', 'matter', 'length', 'location']
    list_filter = ["matter", 'category']
    ordering = ["startdatetime"]
    search_fields = ["title"]


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'id')
    ordering = ['name']
