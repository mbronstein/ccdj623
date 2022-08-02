from django.contrib import admin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from admin_auto_filters.filters import AutocompleteFilterFactory
from import_export.admin import ImportExportModelAdmin

from .models import SsOffice, SsStaff
from phonenumber_field.formfields import PhoneNumberField

# class SsStaffInline(admin.TabularInline):
#     model = SsStaff
#     fields = ('last_name', 'first_name', 'salutation','type', 'ssoffice', 'tel', 'tel_ext')
#     list_editable = ('ssoffice', 'type')


# StateFilter = AutocompleteFilterFactory('State', 'state')
# CityFilter = AutocompleteFilterFactory('City', 'city')
# CategoryFilter = AutocompleteFilterFactory('Category', 'category')
SsOfficeFilter = AutocompleteFilterFactory('SS Office', 'ssoffice')


@admin.register(SsOffice)
class SsOfficeAdmin(ImportExportModelAdmin):
    # inlines = [SsStaffInline,]
    list_display = ('display_name', 'type', 'tel_public', 'fax', 'city', 'state')
    list_filter = ['type']
    ordering = ["slug"]
    exclude = ["modified', 'created", 'added_by', 'modified_by', 'description', ]
    search_fields = ['display_name', 'city', 'state']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'id', None) is None:
            obj.added_by = request.user
            obj.created = timezone.now()
        obj.modified = timezone.now()
        obj.modified_by = request.user
        obj.save()


#
#     # formfield_overrides = {
#     #     PhoneNumberField: {'widget': PhoneNumberPrefixWidget},
#     # }

#
@admin.register(SsStaff)
class SsStaffAdmin(ImportExportModelAdmin):
    exclude = ["modified', 'created", 'added_by', 'modified_by']
    search_fields = ["last_name", "ssoffice", 'city', 'state']
    ordering = ["last_name", 'first_name', "ssoffice"]
    # todo add personal fax
    list_display = ('last_name', 'first_name', 'type', 'ssoffice', 'tel', 'tel_ext')
    list_filter = ['type', 'ssoffice', ]

#
#     formfield_overrides = {PhoneNumberField: {'widget': PhoneNumberInternationalFallbackWidget},
#     # }
#
#     list_editable = ("tel_public", "fax")
#
#
# class JurByLocationFormAdmin(admin.ModelAdmin):
#     readonly_fields = ('modified',)
#
# admin.site.register(JurByLocation, JurByLocationFormAdmin)
