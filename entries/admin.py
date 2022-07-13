from .models import EntryCategory, BaseEntry, CallEntry #NoteEntry, CallEntry, DocEntry, SmsEntry, VoicemailEntry, DictationEntry
from django.contrib import admin


@admin.register(EntryCategory)
class EntryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'id']

@admin.register(BaseEntry)
class BaseEntryAdmin(admin.ModelAdmin):
    # raw_id_fields = ['category']
    list_display = ['datetime', 'matter', 'title', 'category', 'notes','timespent' ]


#
# @admin.register(NoteEntry)
# class NoteEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category', 'description']

#
# #
#
#
# @admin.register(VoicemailEntry)
# class VoicemailEntryAdmin(admin.ModelAdmin):
#     list_display = ['datetime', 'matter',  'title', 'category']

#
# @admin.register(DictationEntry)
# class DictationEntryAdmin(admin.ModelAdmin):
#     list_display = ['matter', 'datetime', 'title', 'category', 'description']
#
#
# @admin.register(DocEntry)
# class DocEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category', 'description']
#
#
# @admin.register(SmsEntry)
# class SmsEntryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'category', 'description']
