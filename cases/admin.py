from django.contrib import admin

from .models import TestSuite, TestCase, TestStep, ParamVariable, HeaderVariable, FormVariable, MultipartVariable, RawData, BinaryData
# from .models import TestSuite, TestCase, TestStep
from apis.admin import RequestDataInline


class TestCaseInline(admin.TabularInline):
    model = TestCase


class TestStepInline(admin.TabularInline):
    model = TestStep


class ParamVariableInline(admin.TabularInline):
    model = ParamVariable


class HeaderVariableInline(admin.TabularInline):
    model = HeaderVariable


class FormVariableInline(admin.TabularInline):
    model = FormVariable


# class JSONVariableInline(admin.TabularInline):
#     model = JSONVariable


class MultipartVariableInline(admin.TabularInline):
    model = MultipartVariable


class RawDataInline(admin.StackedInline):
    model = RawData


class BinaryDataInline(admin.StackedInline):
    model = BinaryData


@admin.register(TestSuite)
class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'description', 'created', 'modified']
    list_filter = ('project',)
    inlines = [TestCaseInline]


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'suite', 'description', 'created', 'modified']
    list_filter = ('suite',)
    inlines = [TestStepInline]


@admin.register(TestStep)
class TestStepAdmin(admin.ModelAdmin):
    list_display = ['name', 'case', 'description', 'created', 'modified']
    list_filter = ('case',)
    inlines = [ParamVariableInline, HeaderVariableInline, FormVariableInline, MultipartVariableInline, RawDataInline, BinaryDataInline]
    # inlines = [RequestDataInline]
