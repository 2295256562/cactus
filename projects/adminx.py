import xadmin
from xadmin import views

from .models import Project, Env, EnvVariable, EnvHeader, Tag


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '接口管理系统'
    site_footer = 'SuperHin'
    menu_style = 'accordion'


class EnvInline(object):
    model = Env


class TagInline(object):
    model = Tag


class ProjectAdmin(object):
    list_display = ['name', 'description', 'created', 'modified']
    inlines = [EnvInline, TagInline]


class EnvVariableInline(object):
    model = EnvVariable


class EnvHeaderInline(object):
    model = EnvHeader


class EnvAdmin(object):
    list_display = ['name', 'project', 'created', 'modified']
    list_filter = ['project']
    inlines = [EnvVariableInline, EnvHeaderInline]


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

xadmin.site.register(Project, ProjectAdmin)
xadmin.site.register(Env, EnvAdmin)
