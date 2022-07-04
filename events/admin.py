from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "type", 'startdatetime', 'length', "matter")
    list_filter = ("matter", "type")
    # ordering = ( "due_date",)
    search_fields = ("title", "matter", "type")
    # actions = [export_to_csv]


admin.site.register(Event, EventAdmin)