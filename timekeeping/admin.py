from django.contrib import admin
from .models import WorkSession


@admin.register(WorkSession)
class WorkSessionAdmin(admin.ModelAdmin):
    pass

    # exclude = ('title', 'created', 'modified', 'modified_by', 'added_by')
    # list_display = ['datetime', 'start_time', 'end_time', 'duration']
    # fields = ('datetime', 'start_time', 'end_time', 'duration', 'notes')
