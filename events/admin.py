from django.contrib import admin
from events.models import Event, EventCategory


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title',  'category', 'matter', 'startdatetime', 'length', 'location']
    list_filter = ["matter", 'category']
    ordering = ["startdatetime"]
    search_fields = ["title"]
    # actions = [export_to_csv]


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'id')
    ordering = ['name']
