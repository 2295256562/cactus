from django.urls import path
from api_test import views

app_name = 'api_test'   # 指定命名空间

LIST_VIEW = dict(get='list', post='create')
DETAIL_VIEW = dict(get='retrieve', put='update', delete='destroy')
RUN_VIEW = dict(get='run')
PARSE_VIEW = dict(get='parse')
COPY_VIEW = dict(get='copy')

urlpatterns = [
    path('projects/', views.Project.as_view(LIST_VIEW), name='projects'),
    path('projects/<pk>/', views.Project.as_view(DETAIL_VIEW), name='project'),

    path('envs/', views.Env.as_view(LIST_VIEW), name='envs'),
    path('envs/<pk>/', views.Env.as_view(DETAIL_VIEW), name='env'),

    path('tags/', views.Tag.as_view(LIST_VIEW), name='tags'),
    path('tags/<pk>/', views.Tag.as_view(DETAIL_VIEW), name='tag'),

    path('variables/', views.Variable.as_view(LIST_VIEW), name='variables'),
    path('variables/<pk>/', views.Variable.as_view(DETAIL_VIEW), name='variable'),

    path('api_categories/', views.ApiCategory.as_view(LIST_VIEW), name='api_categories'),
    path('api_categories/<pk>/', views.ApiCategory.as_view(DETAIL_VIEW), name='api_category'),

    path('apis/', views.Api.as_view(LIST_VIEW), name='apis'),
    path('api/<pk>/', views.Api.as_view(DETAIL_VIEW), name='api'),

    path('testcases/', views.TestCase.as_view(LIST_VIEW), name='testcases'),
    path('testcases/<pk>/', views.TestCase.as_view(DETAIL_VIEW), name='testcase'),
    path('testcases/<pk>/parse/', views.TestCase.as_view(PARSE_VIEW), name='testcase'),
    path('testcases/<pk>/run/', views.TestCase.as_view(RUN_VIEW), name='testcase'),
    path('testcases/<pk>/copy/', views.TestCase.as_view(COPY_VIEW), name='testcase'),

    path('teststeps/', views.TestStep.as_view(LIST_VIEW), name='teststeps'),
    path('teststeps/<pk>/', views.TestStep.as_view(DETAIL_VIEW), name='teststep'),
    path('teststeps/<pk>/parse/', views.TestStep.as_view(PARSE_VIEW), name='teststep'),
    path('teststeps/<pk>/run/', views.TestStep.as_view(RUN_VIEW), name='teststep'),
    path('teststeps/<pk>/copy/', views.TestStep.as_view(COPY_VIEW), name='teststep'),

    path('testsuites/', views.TestSuite.as_view(LIST_VIEW), name='testsuites'),
    path('testsuites/<pk>/', views.TestSuite.as_view(DETAIL_VIEW), name='testsuite'),
    path('testsuites/<pk>/parse/', views.TestSuite.as_view(PARSE_VIEW), name='teststep'),
    path('testsuites/<pk>/run/', views.TestSuite.as_view(RUN_VIEW), name='teststep'),
    path('testsuites/<pk>/copy/', views.TestSuite.as_view(COPY_VIEW), name='teststep'),

    path('testreports/', views.TestReport.as_view(LIST_VIEW), name='testreports'),
    path('testreports/<pk>/', views.TestReport.as_view(DETAIL_VIEW), name='testreport'),

    path('tasks/', views.Task.as_view(LIST_VIEW), name='tasks'),
    path('tasks/<pk>/', views.Task.as_view(DETAIL_VIEW), name='task'),
]
