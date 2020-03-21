from django.contrib import admin

from .models import Project, Env, EnvVariable, EnvHeader, Tag, ProjectVariable, ProjectHeader


class EnvInline(admin.TabularInline):
    model = Env


class TagInline(admin.TabularInline):
    model = Tag


class ProjectVariableInline(admin.TabularInline):
    model = ProjectVariable


class ProjectHeaderInline(admin.TabularInline):
    model = ProjectHeader


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'modified']
    inlines = [ProjectVariableInline, ProjectHeaderInline, EnvInline, TagInline]


class EnvVariableInline(admin.TabularInline):
    model = EnvVariable


class EnvHeaderInline(admin.TabularInline):
    model = EnvHeader


@admin.register(Env)
class EnvAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'created', 'modified']
    list_filter = ['project']
    inlines = [EnvVariableInline, EnvHeaderInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'created', 'modified']
    list_filter = ['project']
