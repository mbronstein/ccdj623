from django.contrib import admin
from .models import MatterType, Matter


class MatterTypeAdmin(admin.ModelAdmin):
    pass

class MatterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Matter, MatterAdmin)
admin.site.register(MatterType, MatterTypeAdmin)
