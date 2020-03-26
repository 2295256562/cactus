from django.contrib import admin

from api_test import models


class EnvInline(admin.TabularInline):
    model = models.Env
    extra = 1


class TagInline(admin.TabularInline):
    model = models.Tag
    extra = 1


class VariableInline(admin.TabularInline):
    model = models.Variable
    extra = 1


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'modified']
    inlines = [TagInline, EnvInline, VariableInline]


class ApiInline(admin.TabularInline):
    model = models.Api
    extra = 1


@admin.register(models.ApiCategory)
class ApiCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
    inlines = [ApiInline]


class TestStepInline(admin.StackedInline):
    model = models.TestStep
    extra = 1
    fieldsets = (
        ['Main', {
            'fields': ('name', 'description', 'case', 'order', 'api', 'skip', 'request'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('extract','check'),
        }]

    )


@admin.register(models.TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
    inlines = [TestStepInline]
    actions = ['run', 'copy']
    def run(self, request, queryset):
        for case in queryset:
            case.run(env_id=1)

    def copy(self, request, queryset):
        for case in queryset:
            case.copy()


@admin.register(models.TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
    actions = ['run', 'copy']

    def run(self, request, queryset):
        for suite in queryset:
            suite.run(env_id=1)

    def copy(self, request, queryset):
        for suite in queryset:
            suite.copy()


@admin.register(models.TestReport)
class TestReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
