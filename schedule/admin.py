from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'energy']
    fields = ['name', 'description', 'energy']
#    radio_fields = {'energy': admin.HORIZONTAL}


admin.site.register(Task, TaskAdmin)



