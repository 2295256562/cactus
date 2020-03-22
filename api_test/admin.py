from django.contrib import admin

import models


class EnvInline(admin.TabularInline):
    model = models.Env


class TagInline(admin.TabularInline):
    model = models.Tag


class VariableInline(admin.TabularInline):
    model = models.Variable


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created', 'modified']
    inlines = [TagInline, EnvInline, VariableInline]


class ApiInline(admin.TabularInline):
    model = models.Api


@admin.register(models.ApiCategory)
class ApiCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
    inlines = [ApiInline]


class TestStepInline(admin.TabularInline):
    model = models.TestStep


@admin.register(models.TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'tags', 'description', 'created', 'modified']
    inlines = [TestStepInline]


@admin.register(models.TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']


@admin.register(models.TestReport)
class TestReportAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
