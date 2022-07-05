from django.contrib import admin
from events.models import Event, EventType


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'matter', 'startdatetime']
    list_filter = ["matter", 'type']
    ordering = [ "startdatetime"]
    search_fields = ["title"]
    # actions = [export_to_csv]

class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id')
    ordering = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)