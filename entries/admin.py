from django.contrib import admin

from entries import EntryCategory, NoteEntry, CallEntry, TimeEntry

#
# @admin.register(EntryCategory)
# class EntryCategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'type', 'description']
#
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

# @admin.register(EmailEntry)
# class EmailEntryAdmin(admin.ModelAdmin):
#     base_model = EmailEntry  # Explicitly set here!
#     show_in_index = True
#
