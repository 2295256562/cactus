from django.contrib import admin

from .models import ApiGroup, Api, ApiDoc


class ApiInline(admin.TabularInline):
    model = Api


class ApiDocInline(admin.StackedInline):
    model = ApiDoc


@admin.register(ApiGroup)
class ApiGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
    list_filters = ['project']
    inlines = [ApiInline]


@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'description', 'created', 'modified']
    list_filters = ['group']
    inlines = [ApiDocInline]


@admin.register(ApiDoc)
class ApiDocAdmin(admin.ModelAdmin):
    list_display = ['api', 'created', 'modified']
