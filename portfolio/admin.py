from django.contrib import admin
from .models import Category, Info, Skill, Project, Contact

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug'
    )

class InfoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nick_name',
        'email',
    )

class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'skill_name',
        'skill_image'
    )

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'project_description',
        'project_date',
        'project_link'
    )

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'from_email',
        'subject',
        'message'
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
