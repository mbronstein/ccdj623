from django.contrib import admin
from .models import Sop,SopStep


@admin.register(SopStep)
class SopStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']


@admin.register(Sop)
class SopAdmin(admin.ModelAdmin):
    list_display = ['title','description' ]
