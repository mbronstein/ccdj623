from django.contrib import admin
from .models import Matter

class MatterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Matter, MatterAdmin)