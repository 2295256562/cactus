from django.contrib import admin

from .models import Project, Env, EnvVariable, EnvHeader, Tag


class EnvInline(admin.TabularInline):
    model = Env


class TagInline(admin.TabularInline):
    model = Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'modified']
    inlines = [EnvInline, TagInline]


class EnvVariableInline(admin.TabularInline):
    model = EnvVariable


class EnvHeaderInline(admin.TabularInline):
    model = EnvHeader


@admin.register(Env)
class EnvAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'created', 'modified']
    list_filter = ['project']
    inlines = [EnvVariableInline, EnvHeaderInline]
