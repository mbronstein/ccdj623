from .models import EntryCategory, BaseEntry, NoteEntry, CallEntry, DocEntry, SmsEntry
from django.contrib import admin


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'id']

#
# @admin.register(BaseEntry)
# class BaseEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category', 'matter']


@admin.register(NoteEntry)
class NoteEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(CallEntry)
class CallEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(SmsEntry)
class SmsEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(DocEntry)
class DocEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']
