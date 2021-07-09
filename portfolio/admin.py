from django.contrib import admin
from .models import Info, Skill, Work, InternshipWork, FreelanceWork, Activity, Contact

class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nick_name',
        'email',
    )

class SkillAdmin(admin.ModelAdmin):
    display = (
        'skill_name'
    )

class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_description',
        'project_date',
        'project_link'
    )

class InternshipWorkAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_description',
        'project_date',
        'project_link'
    )

class FreelanceWorkAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_description',
        'project_date',
        'project_link'
    )

class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'activity_name',
        'activity_description',
        'activity_date',
        'activity_link'
    )

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'from_email',
        'subject',
        'message'
    )

admin.site.register(Info, InfoAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(InternshipWork, InternshipWorkAdmin)
admin.site.register(FreelanceWork, FreelanceWorkAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Contact, ContactAdmin)
