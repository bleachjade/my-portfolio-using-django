from django.contrib import admin
from .models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nick_name',
        'email',
    )

admin.site.register(Info, InfoAdmin)
