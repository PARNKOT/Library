from django.contrib import admin
from mainApp.models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ['number', 'name']


class ProjectAdminSets(admin.ModelAdmin):
    fieldsets = [
        ("Numeric", {"fields": ['number']}),
        ("Text", {"fields": ["name"]}),
    ]


# Register your models here.
admin.site.register(Project)