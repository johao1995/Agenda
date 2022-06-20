from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'last_name',
        'phone',
        'mobile',
        'company',
        'email',
        'date',
        'notes'
    )
admin.site.register(Contact,ContactAdmin)