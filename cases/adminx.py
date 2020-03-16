# import xadmin
# from django.contrib import admin

# from .models import TestSuite, TestCase, TestStep, ParamVariable, HeaderVariable, FormVariable, JSONVariable, MultipartVariable, RawData, BinaryData


# class TestCaseInline(object):
#     model = TestCase


# class TestStepInline(object):
#     model = TestStep


# class ParamVariableInline(object):
#     model = ParamVariable


# class HeaderVariableInline(object):
#     model = HeaderVariable


# class FormVariableInline(object):
#     model = FormVariable


# class JSONVariableInline(object):
#     model = JSONVariable


# class MultipartVariableInline(object):
#     model = MultipartVariable


# class RawDataInline(object):
#     model = RawData


# class BinaryDataInline(object):
#     model = BinaryData


# class TestSuiteAdmin(object):
#     list_display = ['name', 'project', 'description', 'created', 'modified']
#     list_filter = ('project',)
#     inlines = [TestCaseInline]


# class TestCaseAdmin(object):
#     list_display = ['name', 'suite', 'description', 'created', 'modified']
#     list_filter = ('suite',)
#     inlines = [TestStepInline]


# class TestStepAdmin(object):
#     list_display = ['name', 'case', 'description', 'created', 'modified']
#     list_filter = ('case',)
#     inlines = [ParamVariableInline, HeaderVariableInline, FormVariableInline, JSONVariableInline, MultipartVariableInline, RawDataInline, BinaryDataInline]


# xadmin.site.register(TestSuite, TestSuiteAdmin)
# xadmin.site.register(TestCase, TestCaseAdmin)
# xadmin.site.register(TestStep, TestStepAdmin)
