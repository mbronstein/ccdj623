from django.contrib import admin
from .models import Sop, SopStep, SopStepCategory


@admin.register(SopStep)
class SopStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url', 'id']


@admin.register(Sop)
class SopAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'notes', 'steps']


@admin.register(SopStepCategory)
class SopStepCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'id')
    ordering = ['name']
