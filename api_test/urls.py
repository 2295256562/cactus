from django.urls import path
from api_test import views

app_name = 'api_test'   # 指定命名空间

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='projects'),
    path('projects/<pk>/', views.ProjectDetail.as_view(), name='project'),
    path('envs/', views.EnvList.as_view(), name='envs'),
    path('envs/<pk>/', views.EnvDetail.as_view(), name='env'),
    path('tags/', views.TagList.as_view(), name='tags'),
    path('tags/<pk>/', views.TagDetail.as_view(), name='tag'),
    path('variables/', views.VariableList.as_view(), name='variables'),
    path('variables/<pk>/', views.VariableDetail.as_view(), name='variable'),

    path('api_categories/', views.ApiCategoryList.as_view(), name='api_categories'),
    path('api_categories/<pk>/', views.ApiCategoryDetail.as_view(), name='api_category'),
    path('apis/', views.ApiList.as_view(), name='apis'),
    path('api/<pk>/', views.ApiDetail.as_view(), name='api'),

    path('testcases/', views.TestCaseList.as_view(), name='testcases'),
    path('testcases/<pk>/', views.TestCaseDetail.as_view(), name='testcase'),
    path('teststeps/', views.TestStepList.as_view(), name='teststeps'),
    path('teststeps/<pk>/', views.TestStepDetail.as_view(), name='teststep'),

    path('testsuites/', views.TestSuiteList.as_view(), name='testsuites'),
    path('testsuites/<pk>/', views.TestSuiteDetail.as_view(), name='testsuite'),
    path('testreports/', views.TestReportList.as_view(), name='testreports'),
    path('testreports/<pk>/', views.TestReportDetail.as_view(), name='testreport'),
]
