# import xadmin
# from django.contrib import admin

# from .models import ApiGroup, Api, ApiDoc


# class ApiInline(object):
#     model = Api


# class ApiDocInline(object):
#     model = ApiDoc


# # @admin.register(ApiGroup)
# class ApiGroupAdmin(object):
#     list_display = ['name', 'project', 'description', 'created', 'modified']
#     list_filters = ['project']
#     inlines = [ApiInline]


# # @admin.register(Api)
# class ApiAdmin(object):
#     list_display = ['name', 'group', 'description', 'created', 'modified']
#     list_filters = ['group']
#     inlines = [ApiDocInline]


# # @admin.register(ApiDoc)
# class ApiDocAdmin(object):
#     list_display = ['api', 'created', 'modified']


# xadmin.site.register(ApiGroup, ApiGroupAdmin)
# xadmin.site.register(Api, ApiAdmin)
# xadmin.site.register(ApiDoc, ApiDocAdmin)
