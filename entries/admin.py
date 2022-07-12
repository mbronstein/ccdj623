from .models import EntryCategory, BaseEntry, NoteEntry, CallEntry, DocEntry, SmsEntry, VoicemailEntry, DictationEntry
from django.contrib import admin


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'id']



@admin.register(NoteEntry)
class NoteEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(CallEntry)
class CallEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(VoicemailEntry)
class VoicemailEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(DictationEntry)
class DictationEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(DocEntry)
class DocEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']


@admin.register(SmsEntry)
class SmsEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description']
