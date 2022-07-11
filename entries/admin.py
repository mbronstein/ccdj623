from .models import EntryCategory
from django.contrib import admin

@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'id']

#
# @admin.register(NoteEntry)
# class NoteEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'type', 'description']
#
#
# @admin.register(CallEntry)
# class CallEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'type', 'description']
#
#
# @admin.register(TimeEntry)
# class TimeEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'type', 'description']
