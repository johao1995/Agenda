from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'title',
        'description',
        'date',
        'estimated_end',
        'priorty'
    )
admin.site.register(Todo,TodoAdmin)