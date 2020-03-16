from django.contrib import admin

from .models import ApiGroup, Api, ApiDoc

# from .models import RequestData, ParamVariable, HeaderVariable, FormVariable, JSONVariable, MultipartVariable, RawData, BinaryData
from .models import RequestData, ParamVariable, HeaderVariable, FormVariable, MultipartVariable, RawData, BinaryData


class RequestDataInline(admin.TabularInline):
    model = RequestData


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


class RawDataInline(admin.TabularInline):
    model = RawData


class BinaryDataInline(admin.TabularInline):
    model = BinaryData


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


@admin.register(RequestData)
class RequestDataAdmin(admin.ModelAdmin):
    list_display = ['api', 'created', 'modified']
    inlines = [ParamVariableInline, HeaderVariableInline, FormVariableInline, MultipartVariableInline, RawDataInline, BinaryDataInline]
