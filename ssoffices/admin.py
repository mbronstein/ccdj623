from django.contrib import admin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from admin_auto_filters.filters import AutocompleteFilter
from import_export.admin import ImportExportModelAdmin
from .models import SsOffice, SsStaff


# class SsStaffInline(admin.TabularInline):
#     model = SsStaff
#     fields = ('last_name', 'first_name', 'salutation','type', 'ssoffice', 'tel', 'tel_ext')
#     list_editable = ('ssoffice', 'type')


class StateFilter(AutocompleteFilter):
    title = 'State'
    field_name = 'state'


class SsOfficeAdmin(admin.ModelAdmin):

    # inlines = [SsStaffInline,]
    list_display = ( 'display_name', 'type', 'tel_public', 'fax', 'city', 'state')
    list_filter = ['city', 'state', 'type']
    ordering = ["slug"]
    exclude = ["modified', 'created", 'added_by', 'modified_by', 'description', ]
    search_fields = ["slug"]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()


    # formfield_overrides = {
    #     PhoneNumberField: {'widget': PhoneNumberPrefixWidget},
    # }




admin.site.register(SsOffice, SsOfficeAdmin)


class SsStaffAdmin(ImportExportModelAdmin):
    exclude = ["modified', 'created", 'added_by', 'modified_by']
    search_fields = ["last_name", "slug"]
    ordering = ["last_name", 'first_name', "ssoffice"]
    #todo add personal fax
    list_display = ('last_name', 'first_name', 'type', 'salutation','ssoffice','tel', 'tel_ext',
                    )
    # list_filter = ['ssoffice']

    #
    # formfield_overrides = {
    #     PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget},
    # # }

    # list_editable = ("tel_public", "fax")



admin.site.register(SsStaff, SsStaffAdmin)
#
# class JurByLocationFormAdmin(admin.ModelAdmin):
#     readonly_fields = ('modified',)
#
# admin.site.register(JurByLocation, JurByLocationFormAdmin)
