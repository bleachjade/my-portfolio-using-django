from django.contrib import admin
from .models import Info, Work, Contact

class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nick_name',
        'email',
    )

class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_description',
        'github_project'
    )

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'from_email',
        'subject',
        'message'
    )

admin.site.register(Info, InfoAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Contact, ContactAdmin)
