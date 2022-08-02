# from https://github.com/shacker/django-todo
import csv
from django.contrib import admin
from django.utils import timezone
from .models import TaskCategory, Task
from admin_auto_filters.filters import AutocompleteFilterFactory

MatterFilter = AutocompleteFilterFactory('Matter', 'matter')
CategoryFilter = AutocompleteFilterFactory('Category', 'category')


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", 'type', 'description', 'id']
    list_editable = ["type", 'description']
    exclude = ["created", "modified", "added_by", "modified_by", ]
    ordering = ["name"]
    list_filter = ['type']
    search_fields = ["name"]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['compact_due_date', "title", "matter",
                    "priority", "assigned_to", "completed"]
    list_editable = ['title', 'priority', 'completed','assigned_to']
    exclude = ["created", "modified", "added_by", "modified_by", ]  # TODO change added_by to created_by
    fields = ['matter', "datetime",  'category', 'title',  'due_date', 'priority', 'notes',
              "assigned_to",  "completed"]

    ordering = ["due_date"]
    list_filter = [MatterFilter, CategoryFilter, 'due_date', 'priority']

    search_fields = ["title"]

    # actions = [export_to_csv]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()
#
#
# # #
# # # def export_to_csv(modeladmin, request, queryset):
# # #     opts = modeladmin.model._meta
# # #     content_disposition = f"attachment; filename={opts.verbose_name}.csv"
# # #     response = HttpResponse(content_type="text/csv")
# # #     response["Content-Disposition"] = content_disposition
# # #     writer = csv.writer(response)
# # #     fields = [
# # #         field for field in opts.get_fields() if not (field.many_to_many and not field.one_to_many)
# # #     ]
# # #     # Write a first row with header information
# # #     writer.writerow([field.verbose_name for field in fields])
# # #     # Write data rows
# # #     for obj in queryset:
# # #         data_row = []
# # #         for field in fields:
# # #             value = getattr(obj, field.name)
# # #             if isinstance(value, datetime.datetime):
# # #                 value = value.strftime("%d/%m/%Y")
# # #             data_row.append(value)
# # #         writer.writerow(data_row)
# # #     return response
# # #
# # #
# # # export_to_csv.short_description = "Export to CSV"
# # #
# #
# #
# #
# # class CommentAdmin(admin.ModelAdmin):
# #     list_display = ("author", "date", "snippet")
# #
# #
# # @admin.register(Attachment)
# # class AttachmentAdmin(admin.ModelAdmin):
# #     list_display = ("task", "added_by", "timestamp", "file")
# #     autocomplete_fields = ["added_by", "task"]
