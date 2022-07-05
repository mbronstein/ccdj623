from django.contrib import admin
from .models import MatterType, Matter


class MatterTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'id']

class MatterAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']

admin.site.register(Matter, MatterAdmin)
admin.site.register(MatterType, MatterTypeAdmin)
